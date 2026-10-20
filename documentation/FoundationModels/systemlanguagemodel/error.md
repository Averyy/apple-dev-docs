# SystemLanguageModel.Error

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

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

> **Note**: If your app deploys to iOS 26, macOS 26, or visionOS 26, where this error is unavailable, use an availability check and fall back to [`LanguageModelSession.GenerationError.assetsUnavailable(_:)`](../languagemodelsession/generationerror/assetsunavailable%28_%29.md):
>
> ```swift
> do {
>     let response = try await session.respond(to: prompt)
> } catch {
>     if #available(iOS 27.0, macOS 27.0, visionOS 27.0, *),
>         let error = error as? SystemLanguageModel.Error
>     {
>         // Handle the error.
>     } else if case .assetsUnavailable = error as? LanguageModelSession.GenerationError {
>         // Handle the deprecated error.
>     }
> }
> ```

## Topics

### Error cases
- [case assetsUnavailable(SystemLanguageModel.Error.AssetsUnavailable)](./error/assetsunavailable%28_%29.md)
  The assets required for the session are unavailable.
- [SystemLanguageModel.Error.AssetsUnavailable](./error/assetsunavailable.md)
  Information about unavailable model assets.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/error)*