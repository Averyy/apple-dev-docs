# Detecting nudity in media and providing intervention options

**Framework**: Sensitivecontentanalysis

Alert people before displaying images or video that might be sensitive.

#### Overview

In iOS 17 and macOS 14, the Sensitive Content Warning user preference and Communication Safety parental control in Screen Time enable the user to indicate their desire to detect nudity in images and video. To provide people their preferred experience while those settings are active, use the SensitiveContentAnalysis framework to check incoming media before displaying it.

When the framework flags user-provided media as sensitive, intervene by adjusting the user interface in a way that explains the situation and gives the user options to proceed. Avoid displaying flagged content until the user makes a decision.

The Sensitive Content Warning setting is for adults; Communication Safety in Screen Time is intended to protect content on the devices of children. Vary your app’s intervention strategy according to the active setting. For instance, keep interaction brief and unobstructive for adults, whereas for children, use the full view and communicate in age-appropriate language.

The SensitiveContentAnalysis framework doesn’t dictate your user interface. You can tailor your app’s experience according to the examples in apps such as Messages. The following image depicts Messages in iOS 17 when a potentially explicit image arrives from a contact while the Sensitive Content Warning setting is on. Messages blurs the image with a UI that gives the user the option to display the flagged content. It also provides a menu of options to the user, such as blocking the contact or accessing Apple-provided resources on the web for topics like grooming, harassment, and online safety.

![An image of two iPhones side by side that display the Messages app. The phone on the left renders a view of an image that the user received in a conversation. A callout points to the image and contains the text Blurred view. Text referring to the blurred image reads: This may be sensitive. The view contains a button with the text Show and a callout that reads: UI to show content. The phone on the right displays the same conversation in Messages with a detailed image in the view. A callout extends from the detailed image that reads: Shown content. The view contains a button with a warning triangle, from which a callout extends with text that reads: Alternative / additional options.](https://docs-assets.developer.apple.com/published/8f61ec0f4dde803c8f7a0e9c6e87bcbd/detecting_nudity_in_media_and_providing_intervention_options-1%402x.png)

> ❗ **Important**: Apple provides the SensitiveContentAnalysis framework to prevent people from viewing unwanted content, not as a way for an app to report on someone’s behavior. To protect user privacy, don’t transmit any information off the user’s device about whether the SensitiveContentAnalysis framework has identified an image or video as containing nudity. For more information, see the [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/programs/apple-developer-program-license-agreement/#sensitive-content-analysis-framework).

##### Add the App Entitlement

The OS requires the [`com.apple.developer.sensitivecontentanalysis.client`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensitivecontentanalysis.client) entitlement in your app’s code signature to use SensitiveContentAnalysis. Calls to the framework fail to return positive results without it. You can can add this entitlement to your app by enabling the Sensitive Content Analysis capability in Xcode; see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Any team member of the paid App Store developer program can add the entitlement to an app after enabling the capability in Xcode and then signing the Developer Program License Agreement on the [`Accounts`](https://developer.apple.comhttp://developer.apple.com/account) website.

> **Note**: The SensitiveContentAnalysis entitlement is not available for Enterprise development or for people with free accounts.

##### Check Images or Video for Unsafe Content

To check a user-provided image for nudity, create an [`SCSensitivityAnalyzer`](scsensitivityanalyzer.md) object.

```swift
let analyzer = SCSensitivityAnalyzer()
```

An app can utilize the SensitiveContentAnalysis framework by detecting sensitive content when the system sets [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) to either:

- [`SCSensitivityAnalysisPolicy.simpleInterventions`](scsensitivityanalysispolicy/simpleinterventions.md), which indicates that the Sensitive Content Warning user preference is enabled in Settings.
- [`SCSensitivityAnalysisPolicy.descriptiveInterventions`](scsensitivityanalysispolicy/descriptiveinterventions.md), which indicates that the Communication Safety settings is active in Screen Time.

An app can’t leverage the SensitiveContentAnalysis framework when the system sets [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) to [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md). This indicates one or more of the following:

- The app lacks the necessary `com.apple.developer.sensitivecontentanalysis.client` entitlement.
- Neither the Sensitive Content Warning user preference nor the Communication Safety setting in Screen Time are active.
- One of the nudity detection settings are active, but the user disabled sensitive-content warnings for your app in Settings.

If [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md), the SensitiveContentAnalysis framework won’t detect nudity.

```swift
// Check the current analysis policy. 
let policy = analyzer.analysisPolicy
if policy == .disabled { return } 
```

If [`analysisPolicy`](scsensitivityanalyzer/analysispolicy.md) is a value other than [`SCSensitivityAnalysisPolicy.disabled`](scsensitivityanalysispolicy/disabled.md), you can check images or video for sensitive content. To check an image, call one of the `analyzeImage` functions passing in the user-provided image or a URL to an image.

```swift
// Analyze an image file at a particular URL.
let response = try await analyzer.analyzeImage(at: url)

// Analyze an image in memory.
let response = try await analyzer.analyzeImage(image.cgImage)
```

To analyze a video file, pass a video URL into the `videoAnalysis` function and wait on the `hasSensitiveContent` function.

```swift
let handler = analyzer.videoAnalysis(forFileAt: videoFileUrl)
let response = try await handler.hasSensitiveContent()
```

##### Handle Performance Implications

Although sensitivity checks incur additional image processing and introduce a delay while checking video, the presence of active user preferences indicate the user’s expectation to receive protections at the cost of time to review.

Depending on the amount of time that checks take to complete, adjust your app’s UI to accommodate the delay. For example, while checking video for sensitive content, use the `progress` property on the `videoAnalysis` return value to provide the user with status in a custom UI during the process.

```swift
let handler = analyzer.videoAnalysis(forFileAt: videoFileUrl)

// Track analysis and keep the user informed on progress.
let progress = handler.progress
```

##### Tailor User Interface for the Sensitive Content Warning Setting

When your app detects sensitive content, present a UI that coordinates with the active `analysisPolicy`.

When the user has enabled the Sensitive Content Warning setting, keep the user interface brief. In addition:

- Display the UI in an unobstructive manner, such as inline with other content instead of using the full screen.
- Provide intervention as the app receives sensitive content from the network but allow the app to transmit unchecked content over the network.

For example, by providing a blurred version of the potentially sensitive image in its normal location, Messages on iOS 17 and later implements  intervention. Messages also keeps the information presented in the UI brief by providing a one-word button to display the image, and an icon button for more options.

![An image of an iPhone displaying the Messages app. The app presents a conversation that contains an image the user received from a contact. The image is blurred, and contains text that reads: This may be sensitive. The image view contains two buttons, from which a callout extends that reads: Brief UI. The first button resides in the upper right corner of the image and contains a warning triangle. The second button resides in the lower right corner and contains the text Show. ](https://docs-assets.developer.apple.com/published/aff13ca2aebbe4383e6af0e5f6ed8d3e/detecting_nudity_in_media_and_providing_intervention_options-2%402x.png)

##### Tailor User Interface for the Communication Safety Parental Control

When a user has enabled the Communication Safety option in Screen Time, intervene in your app as it receives sensitive content over a network, and before transmitting sensitive content over a network.

Display the intervention in a modal view and use child-appropriate language in your UI. For example, Messages on macOS 14 and iOS 17 interrupts the normal flow of the app by presenting a modal sheet that describes flagged content with broadly understood terms, such as “a naked photo”.

![Screenshots of Messages running on two different Apple platforms. The platform on the left is macOS, and on the right, iOS. Each instance of Messages features a intervention flow that consists of a modal view. The view reads: This photo could be sensitive. Are you sure you want to view? The modal view contains text that provides a definition of sensitive content and it also describes the circumstances under which someone may receive sensitive content. Two buttons follow that read: Not Now and I’m Sure. The iOS device displays an additional button in between those two that reads Ways to Get Help.](https://docs-assets.developer.apple.com/published/b21555e2fc7e788859b2d1cf6a0511d6/detecting_nudity_in_media_and_providing_intervention_options-3%402x.png)

In addition, use two consecutive panes. The following image depicts Messages in iOS 17 when a child attempts to view a sensitive photo sent from a contact. Tapping “I’m sure” on the left raises the second pane on the right.

![Screenshots of two modal intervention panes. The pane on the left displays text that reads: This photo could be sensitive. Are you sure you want to view? Two buttons follow that read: Not Now and I’m Sure. The pane on the right displays text that reads: It’s your choice, but make sure you feel safe. Three buttons follow that read: Don’t View, Message a Grown-up, and View.](https://docs-assets.developer.apple.com/published/7cd2fcf8a01b8bcd1140e05a3b997076/detecting_nudity_in_media_and_providing_intervention_options-4%402x.png)

Inline interventions for the Sensitive Content Warning setting aim to interfere minimally with an adult’s workflow while giving them quick access to help resources. The additional navigation required in the Communication Safety setting provides children with the opportunity to make a considered choice, and tries to avoid ever catching them off guard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options)*