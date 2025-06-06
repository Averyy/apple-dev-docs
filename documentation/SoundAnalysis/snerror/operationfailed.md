# operationFailed

**Framework**: Sound Analysis  
**Kind**: property

An error that occurs when the framework fails to analyze audio.

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
static var operationFailed: SNError.Code { get }
```

## See Also

- [static var invalidModel: SNError.Code](snerror/invalidmodel.md)
  An error that indicates the sound classifier’s underlying Core ML model is an invalid model type.
- [static var invalidFormat: SNError.Code](snerror/invalidformat.md)
  An error that indicates the audio data’s format isn’t valid.
- [static var invalidFile: SNError.Code](snerror/invalidfile.md)
  An error that indicates an audio file is invalid.
- [static var unknownError: SNError.Code](snerror/unknownerror.md)
  An error that represents a failure that no other error handles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snerror/operationfailed)*