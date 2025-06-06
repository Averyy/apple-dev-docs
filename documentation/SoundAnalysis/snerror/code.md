# SNError.Code

**Framework**: Sound Analysis  
**Kind**: enum

The enumerated error codes that the Sound Analysis framework produces.

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
enum Code
```

## Topics

### Errors
- [SNError.Code.invalidModel](snerror/code/invalidmodel.md)
  An error that indicates the sound classifier’s underlying Core ML model is an invalid model type.
- [SNError.Code.invalidFormat](snerror/code/invalidformat.md)
  An error that indicates the audio data’s format isn’t valid.
- [SNError.Code.invalidFile](snerror/code/invalidfile.md)
  An error that indicates an audio file is invalid.
- [SNError.Code.operationFailed](snerror/code/operationfailed.md)
  An error that occurs when the framework fails to analyze audio.
- [SNError.Code.unknownError](snerror/code/unknownerror.md)
  An error that represents a failure that no other error handles.
### Initializers
- [init?(rawValue: Int)](snerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SNError](snerror.md)
  An error from the Sound Analysis framework.
- [let SNErrorDomain: String](snerrordomain.md)
  A string that identifies the Sound Analysis error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snerror/code)*