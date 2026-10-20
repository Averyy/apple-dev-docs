# suppressesPlayerRendering

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player object renders the receiver’s output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var suppressesPlayerRendering: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL suppressesPlayerRendering;
```

#### Discussion

When the value of this property is [`false`](../../Swift/false.md) (the default), the player object handles the rendering of the receiver’s associated output. Change the value of this property to [`true`](../../Swift/true.md) to suppress the rendering of the media data associated with this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/suppressesplayerrendering)*