# uuid

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the timecode source.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * uuid;
```

## Discussion

The UUID uniquely identifies this timecode source. It is particularly useful when multiple sources of the same type are available, allowing your application to distinguish between them.

> **Note**: This value does not persist across application sessions.

## See Also

### Inspecting the source
- [var displayName: String](./displayname.md)
  The name of the timecode source.
- [var type: AVCaptureTimecode.SourceType](./type.md)
  The type of timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source/uuid)*