# MTLCaptureError

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLCaptureError : NSInteger;
```

## Topics

### Errors
- [MTLCaptureError.alreadyCapturing](./mtlcaptureerror/alreadycapturing.md)
  A capture error that indicates the session is already in progress.
- [MTLCaptureError.invalidDescriptor](./mtlcaptureerror/invaliddescriptor.md)
  A capture error that indicates your descriptor has invalid properties.
- [MTLCaptureError.notSupported](./mtlcaptureerror/notsupported.md)
  A capture error that indicates the capture options you’re requesting aren’t available.
### Initializers
- [init?(rawValue: Int)](./mtlcaptureerror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Capture errors
- [let MTLCaptureErrorDomain: String](./mtlcaptureerrordomain.md)
  The error domain for capture errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcaptureerror)*