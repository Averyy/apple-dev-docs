# SystemLanguageModel

**Framework**: Foundation Models  
**Kind**: class

An on-device large language model capable of text generation tasks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class SystemLanguageModel
```

## Mentions

- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)

#### Overview

The `SystemLanguageModel` refers to the on-device text foundation model that powers Apple Intelligence. Use [`default`](systemlanguagemodel/default.md) to access the base version of the model and perform general-purpose text generation tasks. To access a specialized version of the model, initialize the model with [`SystemLanguageModel.UseCase`](systemlanguagemodel/usecase.md) to perform tasks like [`contentTagging`](systemlanguagemodel/usecase/contenttagging.md). Apple will periodically update `SystemLanguageModel` in routine OS updates to improve the on-device model’s abilities and performance. Currently there are 2 model versions that align with:

- iOS, iPadOS, macOS, and visionOS **26.0 - 26.3**
- iOS, iPadOS, macOS, visionOS **26.4**

To better understand the impact of model version on your app, see the guide [`Updating prompts for new model versions`](updating-prompts-for-new-model-versions.md).

Before you use the model, you’ll need to verify its availability. Model availability depends on device factors like:

- The device must support Apple Intelligence.
- Apple Intelligence must be turned on in Settings.

Use [`SystemLanguageModel.Availability`](systemlanguagemodel/availability-swift.enum.md) to change what your app shows to people based on the availability condition:

```swift
struct GenerativeView: View {
    // Create a reference to the system language model.
    private var model = SystemLanguageModel.default

    var body: some View {
        switch model.availability {
        case .available:
            // Show your intelligence UI.
        case .unavailable(.deviceNotEligible):
            // Show an alternative UI.
        case .unavailable(.appleIntelligenceNotEnabled):
            // Ask the person to turn on Apple Intelligence.
        case .unavailable(.modelNotReady):
            // The model isn't ready because it's downloading or because
            // of other system reasons.
        case .unavailable(let other):
            // The model is unavailable for an unknown reason.
        }
    }
}
```

## Topics

### Loading the model with a use case
- [convenience init(useCase: SystemLanguageModel.UseCase, guardrails: SystemLanguageModel.Guardrails)](systemlanguagemodel/init(usecase:guardrails:).md)
  Creates a system language model for a specific use case.
- [SystemLanguageModel.UseCase](systemlanguagemodel/usecase.md)
  A type that represents the use case for prompting.
- [SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails.md)
  Guardrails flag sensitive content from model input and output.
### Loading the model with an adapter
- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)
  Specialize the behavior of the system language model by using a custom adapter you train.
- [com.apple.developer.foundation-model-adapter](../BundleResources/Entitlements/com.apple.developer.foundation-model-adapter.md)
  A Boolean value that indicates whether the app can enable custom adapters for the Foundation Models framework.
- [convenience init(adapter: SystemLanguageModel.Adapter, guardrails: SystemLanguageModel.Guardrails)](systemlanguagemodel/init(adapter:guardrails:).md)
  Creates the base version of the model with an adapter.
- [SystemLanguageModel.Adapter](systemlanguagemodel/adapter.md)
  Specializes the system language model for custom use cases.
### Checking model availability
- [var isAvailable: Bool](systemlanguagemodel/isavailable.md)
  A convenience getter to check if the system is entirely ready.
- [var availability: SystemLanguageModel.Availability](systemlanguagemodel/availability-swift.property.md)
  The availability of the language model.
- [SystemLanguageModel.Availability](systemlanguagemodel/availability-swift.enum.md)
  The availability status for a specific system language model.
### Accessing the context size
- [var contextSize: Int](systemlanguagemodel/contextsize.md)
  Returns the maximum context size (in tokens) supported by the model.
### Getting the token count
- [func tokenCount(for:)](systemlanguagemodel/tokencount(for:).md)
  Returns the token count for the specified instructions.
### Retrieving the supported languages
- [var supportedLanguages: Set<Locale.Language>](systemlanguagemodel/supportedlanguages.md)
  Languages that the model supports.
### Determining whether the model supports a locale
- [func supportsLocale(Locale) -> Bool](systemlanguagemodel/supportslocale(_:).md)
  Returns a Boolean indicating whether the given locale is supported by the model.
### Getting the default model
- [static var `default`: SystemLanguageModel](systemlanguagemodel/default.md)
  The base version of the model.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Foundation Models updates](../Updates/FoundationModels.md)
  Learn about important changes to Foundation Models.
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
  Enhance the experience in your app by prompting an on-device large language model.
- [Adding intelligent app features with generative models](adding-intelligent-app-features-with-generative-models.md)
  Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel)*