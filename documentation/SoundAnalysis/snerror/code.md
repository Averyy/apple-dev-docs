# SNError.Code

**Framework**: Sound Analysis  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum SNErrorCode : NSInteger;
```

## Topics

### Errors
- [SNError.Code.invalidModel](./code/invalidmodel.md)
  An error that indicates the sound classifier’s underlying Core ML model is an invalid model type.
- [SNError.Code.invalidFormat](./code/invalidformat.md)
  An error that indicates the audio data’s format isn’t valid.
- [SNError.Code.invalidFile](./code/invalidfile.md)
  An error that indicates an audio file is invalid.
- [SNError.Code.operationFailed](./code/operationfailed.md)
  An error that occurs when the framework fails to analyze audio.
- [SNError.Code.unknownError](./code/unknownerror.md)
  An error that represents a failure that no other error handles.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct SNError](../snerror.md)
  An error from the Sound Analysis framework.
- [let SNErrorDomain: String](../snerrordomain.md)
  A string that identifies the Sound Analysis error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snerror/code)*