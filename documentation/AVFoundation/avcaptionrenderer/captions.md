# captions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The captions to render.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var captions: [AVCaption] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVCaption *> * captions;
```

#### Discussion

This property value is an empty array if there are no captions for the system to render.

## See Also

### Configuring the renderer
- [var bounds: CGRect](./bounds.md)
  The drawing bounds of caption scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captions)*