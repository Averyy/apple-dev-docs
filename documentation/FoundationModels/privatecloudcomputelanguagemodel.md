# PrivateCloudComputeLanguageModel

**Framework**: Foundation Models  
**Kind**: class

A variant of Apple Foundation Models that runs on Private Cloud Compute to provide enhanced capabilities while maintaining privacy guarantees.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class PrivateCloudComputeLanguageModel
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)
- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)

#### Overview

To use the server-based model that powers Apple Intelligence, you change a single line of code that you apply when creating your [`LanguageModelSession`](languagemodelsession.md).

```swift
// Create a session with the server-side model.
let session = LanguageModelSession(model: PrivateCloudComputeLanguageModel())
let response = try await session.respond(to: "Analyze this document...")
```

Before using the model, verify its availability. Model availability depends on whether the device and region supports Apple Intelligence. For a list of supported devices, see [`Apple Intelligence`](https://developer.apple.comhttps://www.apple.com/apple-intelligence/).

> ❗ **Important**: To develop with PCC you must meet certain eligibility requirements. To learn more and request access to the managed entitlement, see [`Accessing Private Cloud Compute`](https://developer.apple.comhttps://developer.apple.com/private-cloud-compute/).

## Topics

### Creating an instance
- [convenience init()](privatecloudcomputelanguagemodel/init.md)
  Creates a Private Cloud Compute language model instance.
### Inspecting the availability
- [var isAvailable: Bool](privatecloudcomputelanguagemodel/isavailable.md)
  A Boolean value that indicates whether the system is entirely ready.
- [var availability: PrivateCloudComputeLanguageModel.Availability](privatecloudcomputelanguagemodel/availability-swift.property.md)
  The availability of the language model.
- [PrivateCloudComputeLanguageModel.Availability](privatecloudcomputelanguagemodel/availability-swift.enum.md)
  The availability status for a specific PCC language model.
### Getting the quota
- [var quotaUsage: PrivateCloudComputeLanguageModel.QuotaUsage](privatecloudcomputelanguagemodel/quotausage-swift.property.md)
  The usage quota for this model.
- [PrivateCloudComputeLanguageModel.QuotaUsage](privatecloudcomputelanguagemodel/quotausage-swift.struct.md)
  The usage quota state for a Private Cloud Compute language model.
### Accessing the context size
- [var contextSize: Int](privatecloudcomputelanguagemodel/contextsize.md)
  The maximum context size in tokens supported by the model.
### Handling language and locales
- [var supportedLanguages: Set<Locale.Language>](privatecloudcomputelanguagemodel/supportedlanguages.md)
  Languages that the model supports.
- [func supportsLocale(Locale) async throws -> Bool](privatecloudcomputelanguagemodel/supportslocale(_:).md)
  Returns a Boolean value that indicates whether the given locale is supported by the model.
### Accessing the error
- [PrivateCloudComputeLanguageModel.Error](privatecloudcomputelanguagemodel/error.md)
  Errors that may occur when using Private Cloud Compute.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [LanguageModel](languagemodel.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)
  Access a larger context window and stronger reasoning by routing session requests through Private Cloud Compute.
- [com.apple.developer.private-cloud-compute](../bundleresources/entitlements/com.apple.developer.private-cloud-compute.md)
  A Boolean value that indicates whether the app can use Private Cloud Compute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel)*