# Translating text within your app

**Framework**: Translation

Display simple system translations and create custom translation experiences.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- Xcode 16.0+

#### Overview

With the Translation framework, you can offer in-app translations from one language to another. To display simple system translations in your app, use the [`translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)`](https://developer.apple.com/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)) translation overlay.

For a more customizable translation experience, use the [`TranslationSession`](translationsession.md) object and its associated translation methods. With the customizable translation APIs, the framework asks a person for permission to download the language translation models, if necessary. You can translate strings efficiently, while checking for language availability before offering a translation.

This sample code project provides the `TranslatingText` sample app to demonstrate various methods of translating text. It consists of the following translation demos:

- Translate Text
- Replace Text
- Single String
- Batch All at Once
- Batch as a Sequence
- Language Availability
- Prepare for Translation

> **Note**: This sample code project is associated with WWDC24 session [`10117: Meet the Translation API`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10117/).

##### Configure the Sample Code Project

Before you run the sample code project, download and install Xcode 16 or later.

> **Note**: This sample code project runs only in macOS and on physical iOS devices. It doesn’t translate text in iOS or iPadOS simulators.

To run the sample code project in macOS, select My Mac from the Xcode toolbar scheme menu, and then choose Project > Run.

To run the sample code on a physical iOS device:

1. Upgrade your device to iOS 18 or later.
2. Select your device from the Xcode toolbar scheme menu.
3. Select the `TranslatingText` project.
4. Click the `TranslatingText` target and select your team from the Team menu in the Signing & Capabilities pane to let Xcode automatically manage your provisioning profile. For more information, see [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).
5. Choose Project > Run.

##### Translate Text with the Simple Translation Overlay

The Translate Text demo shows how to offer a translation using the system UI. The code example below indicates what happens when a person clicks the Translate button in that demo. First, the sample defines a variable to control when the system UI appears using a [`State`](https://developer.apple.com/documentation/SwiftUI/State) property wrapper. Then it defines a variable representing the text to translate. Finally, it passes the `State` property wrapper that controls when the system UI displays along with the text to translate to the [`translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)`](https://developer.apple.com/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)) function that attaches to the view containing the text to translate.

```swift
struct ViewTranslationView: View {
    // Define the condition to display the translation UI.
    @State private var showTranslation = false

    // Define the text you want to translate.
    var originalText = "Hallo, Welt!"

    var body: some View {
        VStack {
            Text(verbatim: originalText)
            Button("Translate") {
                showTranslation.toggle()
            }
        }
        // Offer a system UI translation.
        .translationPresentation(isPresented: $showTranslation,
                                 text: originalText)
        .navigationTitle("Translate")
    }
}
```

The Replace Text demo also uses the system UI, and replaces the original text with the translated text by adding the `replacementAction` trailing closure to the function. This closure runs after the translation occurs when a person clicks the Translate button. The sample then replaces the input text with the translated text.

```swift
.translationPresentation(isPresented: $showTranslation, text: originalText) { translatedText in
    originalText = translatedText
}
```

##### Offer a Custom Translation

For more control over the translation experience, you can create your own in-app translation experiences using the [`TranslationSession`](translationsession.md) object, along with its associated translation functions.

The Single String demo shows how to translate a single string of text and update a view. Its code example below defines a `State` property wrapper for the [`TranslationSession.Configuration`](translationsession/configuration.md) object in the view offering the translation, and passes it to a [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) function. Then it uses the `session` instance the task returns to call [`translate(_:)`](translationsession/translate(_:).md) and passes in the string of text to translate. Finally, it updates the view using the [`targetText`](translationsession/response/targettext.md) property from the response.

```swift
struct SingleStringView: View {
    @State private var sourceText = "Hallo, Welt!"
    @State private var targetText = ""

    // Define a configuration.
    @State private var configuration: TranslationSession.Configuration?

    var body: some View {
        VStack {
            TextField("Enter text to translate", text: $sourceText)
                .textFieldStyle(.roundedBorder)
            Button("Translate") {
                triggerTranslation()
            }
            Text(verbatim: targetText)
        }
        // Pass the configuration to the task.
        .translationTask(configuration) { session in
            do {
                // Use the session the task provides to translate the text.
                let response = try await session.translate(sourceText)

                // Update the view with the translated result.
                targetText = response.targetText
            } catch {
                // Handle any errors.
            }
        }
        .padding()
        .navigationTitle("Single string")
    }

    private func triggerTranslation() {
        guard configuration == nil else {
            configuration?.invalidate()
            return
        }

        // Let the framework automatically determine the language pairing.
        configuration = .init()
    }
}
```

This pattern of defining a configuration as a `State` property wrapper and invalidating its state is recommended for triggering new translations. Storing [`TranslationSession.Configuration`](translationsession/configuration.md) in a model object also works.

##### Translate Batches of Strings

To translate multiple strings between the same languages, it’s most efficient to use one of the batch translation functions of [`TranslationSession`](translationsession.md). You can translate a batch of strings and get the results all at once, or you can receive them incrementally as they arrive.

To keep your UI clean and uncluttered, you can also do this work in a view model, as the Batch All at Once demo shows. Its code example defines a `State` property wrapper for a [`TranslationSession.Configuration`](translationsession/configuration.md) object in the view offering the translation, and attaches the [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) function to the view containing the text to translate. Using the `session` instance from the task, it calls the [`translations(from:)`](translationsession/translations(from:).md) function in the view model. The view model maps all the strings to translate in an array of type [`TranslationSession.Request`](translationsession/request.md) and sets the [`sourceText`](translationsession/request/sourcetext.md) property of the request to the string to translate. Then the sample calls [`translations(from:)`](translationsession/translations(from:).md) on the session object and passes in the array of requests to translate. Finally, it maps each response object that returns to the corresponding index in the original array of text.

When translating a group of strings using the [`translations(from:)`](translationsession/translations(from:).md) function, the responses return in the same order you send them.

##### Display the Results As They Arrive

If you want to translate multiple strings of text and display the results as they arrive, use the [`translate(batch:)`](translationsession/translate(batch:).md) function.

The Batch as a Sequence demo is the same as the Batch All at Once demo except for the way it matches translation requests to responses.

In this process, the responses can return in a different order than you send them. So the Batch as a Sequence demo tracks which request corresponds with which response by assigning a [`clientIdentifier`](translationsession/request/clientidentifier.md) to each sent request — in this case, the index of the item to translate in the array. The client identifier returns with the same value in the response. When the response returns, the sample uses the client identifier to associate the request with the response.

```swift
extension ViewModel {
    func translateSequence(using session: TranslationSession) async {
        Task { @MainActor in
            let requests: [TranslationSession.Request] = foodItems.enumerated().map { (index, string) in
                // Assign each request a client identifier.
                    .init(sourceText: string, clientIdentifier: "\(index)")
            }

            do {
                for try await response in session.translate(batch: requests) {
                    // Use the returned client identifier (the index) to map the request to the response.
                    guard let index = Int(response.clientIdentifier ?? "") else { continue }
                    foodItems[index] = response.targetText
                }
            } catch {
                // Handle any errors.
            }
        }
    }
}
```

##### Check for Language Availability

The Language Availability demo shows how to check whether the framework supports a specific language pairing before offering it to people. A person selects a source and a target language from a picker, and the sample passes that language pairing to a function in the view model that checks whether the framework supports that pairing. The view then updates the display when the model sets the `isTranslationSupported` variable.

```swift
extension ViewModel {
    func checkLanguageSupport(from source: Locale.Language, to target: Locale.Language) async {
        let availability = LanguageAvailability()
        let status = await availability.status(from: source, to: target)

        switch status {
        case .installed, .supported:
            isTranslationSupported = true
        case .unsupported:
            isTranslationSupported = false
        @unknown default:
            print("Not supported")
        }
    }
}
```

> **Note**: The framework doesn’t support translation between the same language, such as British English (en-GB) and U.S. English (en-US).

##### Prepare for Translation

If you know which languages a translation needs, you can download the language models before offering the translation.

The Prepare for Translation demo shows how to initiate the download of a language pairing by creating a `TranslationSession.Configuration` instance with the source and target language to download. The sample then calls [`prepareTranslation()`](translationsession/preparetranslation().md) on the session the translation task returns. If the languages aren’t already downloaded, a view appears that requests permission to download them.

```swift
struct PrepareTranslationView: View {

    // Define the pairing of languages you want to download.
    @State private var configuration = TranslationSession.Configuration(
        source: Locale.Language(identifier: "pt_BR"),
        target: Locale.Language(identifier: "ko_KR")
    )

    @State private var buttonTapped = false

    var body: some View {
        VStack(spacing: 20) {
            Text("Tap the button to start downloading languages before offering a translation.")
            Button("Prepare") {
                configuration.invalidate()
                buttonTapped = true
            }
        }
        .translationTask(configuration) { session in
            if buttonTapped {
                do {
                    // Display a sheet asking the user's permission
                    // to start downloading the language pairing.
                    try await session.prepareTranslation()
                } catch {
                    // Handle any errors.
                }
            }
        }
        .padding()
        .navigationTitle("Prepare translation")
    }
}
```

For testing, you can delete locally downloaded models in macOS by choosing System Settings > General > Language & Region > Translation Languages. In iOS, you can manage your downloaded languages by choosing Settings > Apps > Translate > Downloaded Languages if you have the system Translate app installed locally on your device.

## See Also

- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](../SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](../SwiftUI/View/translationTask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](../SwiftUI/View/translationTask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [class TranslationSession](translationsession.md)
  A class that performs translations between a pair of languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translating-text-within-your-app)*