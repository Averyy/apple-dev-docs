# supportsAdaptiveImageGlyph

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document supports adaptive images in the input.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional var supportsAdaptiveImageGlyph: Bool { get }
```

```objc
@property (readonly) BOOL supportsAdaptiveImageGlyph;
```

#### Discussion

When this property is [`false`](../../Swift/false.md), the input system doesn’t allow the text input to contain adaptive images. Set the value of this property to [`true`](../../Swift/true.md) only if your document supports adaptive images and handles them properly. For more information, see [`NSAdaptiveImageGlyph`](../nsadaptiveimageglyph.md).

## See Also

### Supporting adaptive images
- [func insert(NSAdaptiveImageGlyph, replacementRange: NSRange)](./insert%28_,replacementrange%29.md)
  Inserts an adaptive image into the text at the specifed location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/supportsadaptiveimageglyph)*