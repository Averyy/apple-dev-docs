# conformsCaptionsToTimeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to conform the time range of a canonical caption.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var conformsCaptionsToTimeRange: Bool { get set }
```

```objc
@property (nonatomic) BOOL conformsCaptionsToTimeRange;
```

#### Discussion

By default, this property value is [`false`](../../Swift/false.md). If you set the value to [`true`](../../Swift/true.md), this object conforms the time range of captions to fit its encoded data.

When this object conforms captions to CAE608 format, it encodes them so that each CAE608 2-byte control code fits into one frame duration (1001/30000).

## See Also

### Conforming captions
- [func conformedCaption(for: AVCaption) throws -> AVCaption](./conformedcaption%28for%29.md)
  Creates a caption that conforms to a specific format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/conformscaptionstotimerange)*