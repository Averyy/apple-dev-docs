# MTLCaptureError

**Framework**: Metal  
**Kind**: enum

Errors returned by capture sessions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLCaptureError
```

## Topics

### Errors
- [MTLCaptureError.alreadyCapturing](mtlcaptureerror/alreadycapturing.md)
  A capture session is already in progress.
- [MTLCaptureError.invalidDescriptor](mtlcaptureerror/invaliddescriptor.md)
  The descriptor contained invalid parameters.
- [MTLCaptureError.notSupported](mtlcaptureerror/notsupported.md)
  The requested capture options are not available.
### Initializers
- [init?(rawValue: Int)](mtlcaptureerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let MTLCaptureErrorDomain: String](mtlcaptureerrordomain.md)
  The error domain for capture errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcaptureerror)*