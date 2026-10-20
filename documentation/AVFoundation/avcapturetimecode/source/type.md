# type

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The type of timecode source.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var type: AVCaptureTimecode.SourceType { get }
```

```objc
@property (nonatomic, assign, readonly) AVCaptureTimecodeSourceType type;
```

#### Discussion

Indicates the type of timecode source, represented as a value from the `AVCaptureTimecodeSynchronizationSourceType` enum. This helps you identify the source for specific synchronization use cases, such as frame counter, real-time clock, MIDI, or HID.

## See Also

### Inspecting the source
- [var displayName: String](./displayname.md)
  The name of the timecode source.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source/type)*