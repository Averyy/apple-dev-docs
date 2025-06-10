# SNError

**Framework**: Sound Analysis  
**Kind**: struct

An error from the Sound Analysis framework.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct SNError
```

## Topics

### Error Codes
- [static var invalidModel: SNError.Code](snerror/invalidmodel.md)
  An error that indicates the sound classifier’s underlying Core ML model is an invalid model type.
- [static var invalidFormat: SNError.Code](snerror/invalidformat.md)
  An error that indicates the audio data’s format isn’t valid.
- [static var invalidFile: SNError.Code](snerror/invalidfile.md)
  An error that indicates an audio file is invalid.
- [static var operationFailed: SNError.Code](snerror/operationfailed.md)
  An error that occurs when the framework fails to analyze audio.
- [static var unknownError: SNError.Code](snerror/unknownerror.md)
  An error that represents a failure that no other error handles.
### Error Information
- [SNError.Code](snerror/code.md)
  The enumerated error codes that the Sound Analysis framework produces.
### Error Domain
- [let SNErrorDomain: String](snerrordomain.md)
  A string that identifies the Sound Analysis error domain.
- [static var errorDomain: String](snerror/errordomain.md)
  A statically accessible string that identifies the Sound Analysis error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SNError.Code](snerror/code.md)
  The enumerated error codes that the Sound Analysis framework produces.
- [let SNErrorDomain: String](snerrordomain.md)
  A string that identifies the Sound Analysis error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snerror)*