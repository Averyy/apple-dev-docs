# supportsAdaptiveImageGlyph

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document supports adaptive images in the input.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional var supportsAdaptiveImageGlyph: Bool { get }
```

#### Discussion

When this property is [`false`](https://developer.apple.com/documentation/swift/false), the input system doesn’t allow the text input to contain adaptive images. Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) only if your document supports adaptive images and handles them properly. For more information, see [`NSAdaptiveImageGlyph`](nsadaptiveimageglyph.md).

## See Also

- [func insert(NSAdaptiveImageGlyph, replacementRange: NSRange)](nstextinputclient/insert(_:replacementrange:).md)
  Inserts an adaptive image into the text at the specifed location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/supportsadaptiveimageglyph)*