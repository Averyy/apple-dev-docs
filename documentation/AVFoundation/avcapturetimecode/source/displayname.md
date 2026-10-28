# displayName

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The name of the timecode source.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var displayName: String { get }
```

```objc
@property (nonatomic, copy, readonly, nonnull) NSString * displayName;
```

## Discussion

This property provides a descriptive name of the timecode source, useful for display in user interfaces or logging.

## See Also

### Inspecting the source
- [var type: AVCaptureTimecode.SourceType](./type.md)
  The type of timecode source.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source/displayname)*