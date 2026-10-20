# Optimizing your app for Assistive Access

**Framework**: Accessibility  
**Role**: Article

Adjust your app’s UI to make sure it works well for people who use Assistive Access.

#### Overview

In general, make sure your standard app UI works well for Assistive Access. However, you can make adjustments to your UI to make sure it looks and works as you expect in Assistive Access. You can optimize your UI for Assistive Access in one of these ways:

- Create a streamlined UI by adopting the Assistive Access scene type.
- Get more screen space for your existing UI by opting in to full-screen mode.

Additionally, you can remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

##### Create a streamlined UI for Assistive Access

Adding the [`UISupportsAssistiveAccess`](../BundleResources/information-property-list/uisupportsassistiveaccess.md) key to your project’s Info pane with a value of `YES` indicates your app supports a streamlined experience designed for Assistive Access. It allows your app’s UI to match the prominent style of Assistive Access controls. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app is optimized for this feature.

If you add this key to your project’s Info pane, adopt the [`AssistiveAccess`](../SwiftUI/assistiveaccess.md) scene type to provide a streamlined UI for your app when Assistive Access is on. For example, you can define a custom view hierarchy with fewer onscreen elements.

```swift
import SwiftUI

@main
struct ExampleApp: App {
    var body: some Scene {
        // Defines the default app UI. 
        WindowGroup {
            StandardContentView()
        }
        
        // Defines the app UI when Assistive Access is on.
        AssistiveAccess {
            AssistiveAccessContentView()
        }
    }
}
```

##### Opt in to full-screen mode for your existing UI

Adding the [`UISupportsFullScreenInAssistiveAccess`](../BundleResources/information-property-list/uisupportsfullscreeninassistiveaccess.md) key to your project’s Info pane with a value of `YES` allows your app’s standard UI to expand into all the available space above the Back button in Assistive Access. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app’s UI is optimized for this feature.

If you add this key to your project’s Info pane, ensure your UI is adaptive so that it works with flexible screen dimensions. Don’t rely on fixed screen sizes in your app design or logic. Use safe areas and layout guides to avoid overlapping your app’s UI with system UI or hardware elements. For more information, see [`safeAreaInsets`](../UIKit/uiview/safeareainsets.md) and [`safeAreaLayoutGuide`](../UIKit/uiview/safearealayoutguide.md).

If you don’t add this key to your project’s Info pane, a trusted supporter can still choose to make your app available in Assistive Access. By default, the system draws apps in a reduced frame to fit them onscreen with the prominent Back button in Assistive Access. This frame matches the dimensions of a smaller iPhone or iPad screen, so you don’t need to make changes to your existing UI for your app to work in Assistive Access.

##### Remove unnecessary UI elements

It may not be possible for a person who’s using your app while Assistive Access is running to complete certain tasks or workflows, due to the differences described in [Understand certain differences in Assistive Access on iPhone](https://support.apple.com/guide/assistive-access-iphone/understand-differences-assistive-access-dev473e94873/ios). In situations like this, you can make note of these differences when you test your app in Assistive Access, and remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

To make small adjustments to your UI in Assistive Access, you check whether Assistive Access is running on the device using SwiftUI or the Accessibility framework.

**SwiftUI**:

```swift
import SwiftUI

@Environment(\.accessibilityAssistiveAccessEnabled) private var isAssistiveAccessEnabled

if isAssistiveAccessEnabled {
  // Assistive Access is on. Make small adjustments specific to Assistive Access.
}
```

**Accessibility framework**:

```swift
import Accessibility

if AccessibilitySettings.isAssistiveAccessEnabled {
  // Assistive Access is on. Make small adjustments specific to Assistive Access.
} 
```

For Assistive Access design guidance, read Human Interface Guidelines > [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

#### See Also

###### Related reference

- [`isAssistiveAccessEnabled`](./accessibilitysettings/isassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is running.
- [`accessibilityAssistiveAccessEnabled`](../SwiftUI/environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [`UISupportsFullScreenInAssistiveAccess`](../BundleResources/information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [`AssistiveAccess`](../SwiftUI/assistiveaccess.md)
  A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.
- [`UISupportsAssistiveAccess`](../BundleResources/information-property-list/uisupportsassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app supports Assistive Access.

###### Related articles

- [Performing accessibility testing for your app](./performing-accessibility-testing-for-your-app.md)
  Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.

###### Related design guidance

- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  Accessible user interfaces empower everyone to have a great experience with your app or game.

###### Related videos

- [Customize your app for Assistive Access](https://developer.apple.com/videos/play/wwdc2025/238)
  Assistive Access is a distinctive, focused iOS experience that makes it easier for people with cognitive disabilities to use iPhone and iPad independently. In iOS and iPadOS 26, you can customize your app when it’s running in Assistive Access to give people greater ease and independence. Learn how to tailor your app using the AssistiveAccess SwiftUI scene type, and explore the key design principles that can help you create a high-quality Assistive Access experience for everyone.
- [Meet Assistive Access](https://developer.apple.com/videos/play/wwdc2023/10032)
  Learn how Assistive Access can help people with cognitive disabilities more easily use iPhone and iPad. Discover the design principles that guide Assistive Access and find out how the system experience adapts to lighten cognitive load. We’ll show you how Assistive Access works and what you can do to support this experience in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/optimizing-your-app-for-assistive-access)*