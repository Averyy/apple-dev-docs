# SystemLanguageModel.Error

**Framework**: Foundation Models  
**Kind**: enum

An error specific to the on-device system language model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Error
```

#### Overview

> **Note**: If your app deploys to iOS 26, macOS 26, or visionOS 26, where this error is unavailable, use an availability check and fall back to [`LanguageModelSession.GenerationError.assetsUnavailable(_:)`](languagemodelsession/generationerror/assetsunavailable(_:).md): ```swift
do {
    let response = try await session.respond(to: prompt)
} catch {
    if #available(iOS 27.0, macOS 27.0, visionOS 27.0, *),
        let error = error as? SystemLanguageModel.Error
    {
        // Handle the error.
    } else if case .assetsUnavailable = error as? LanguageModelSession.GenerationError {
        // Handle the deprecated error.
    }
}
```

## Topics

### Error cases
- [case assetsUnavailable(SystemLanguageModel.Error.AssetsUnavailable)](systemlanguagemodel/error/assetsunavailable(_:).md)
  The assets required for the session are unavailable.
- [SystemLanguageModel.Error.AssetsUnavailable](systemlanguagemodel/error/assetsunavailable.md)
  Information about unavailable model assets.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Error](../swift/error.md)
- [Escapable](../swift/escapable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/error)*