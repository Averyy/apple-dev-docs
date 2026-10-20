# insert(_:replacementRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts an adaptive image into the text at the specifed location.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional func insert(_ adaptiveImageGlyph: NSAdaptiveImageGlyph, replacementRange: NSRange)
```

```objc
- (void) insertAdaptiveImageGlyph:(NSAdaptiveImageGlyph *) adaptiveImageGlyph replacementRange:(NSRange) replacementRange;
```

## Parameters

- `adaptiveImageGlyph`: The adaptive image to add to the text.
- `replacementRange`: The text range at which to insert the image.

## See Also

### Supporting adaptive images
- [var supportsAdaptiveImageGlyph: Bool](./supportsadaptiveimageglyph.md)
  A Boolean value that indicates whether the document supports adaptive images in the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/insert(_:replacementrange:))*