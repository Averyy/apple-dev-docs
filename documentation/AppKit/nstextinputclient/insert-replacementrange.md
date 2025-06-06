# insert(_:replacementRange:)

**Framework**: AppKit  
**Kind**: method

Inserts an adaptive image into the text at the specifed location.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional func insert(_ adaptiveImageGlyph: NSAdaptiveImageGlyph, replacementRange: NSRange)
```

## Parameters

- `adaptiveImageGlyph`: The adaptive image to add to the text.
- `replacementRange`: The text range at which to insert the image.

## See Also

- [var supportsAdaptiveImageGlyph: Bool](nstextinputclient/supportsadaptiveimageglyph.md)
  A Boolean value that indicates whether the document supports adaptive images in the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/insert(_:replacementrange:))*