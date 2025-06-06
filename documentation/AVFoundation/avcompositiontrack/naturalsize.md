# naturalSize

**Framework**: AVFoundation  
**Kind**: property

The natural dimensions of the media data that the track references.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var naturalSize: CGSize { get }
```

#### Discussion

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGSize/zero).

## See Also

- [var preferredTransform: CGAffineTransform](avcompositiontrack/preferredtransform.md)
  The track’s transform preference to apply to its visual content during presentation or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/naturalsize)*