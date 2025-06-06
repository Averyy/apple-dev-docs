# naturalSize

**Framework**: AVFoundation  
**Kind**: property

The natural dimensions of the media data that the track references.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var naturalSize: CGSize { get }
```

#### Discussion

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGSize/zero).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/naturalsize)*