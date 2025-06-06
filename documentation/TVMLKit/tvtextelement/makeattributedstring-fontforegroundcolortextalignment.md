# makeAttributedString(font:foregroundColor:textAlignment:)

**Framework**: TVMLKit  
**Kind**: method

Convenience method for configuring an attributed string given the specified attributes.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString
```

#### Return Value

An [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) object with the applied attributes.

#### Discussion

Supply a font to this method to get the [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) representation of the text contained within an element. Use the `foregroundColor` and `alignment` parameters to override the value specified in the text element.

## Parameters

- `font`: The font used for the attributed string. This can be any available font on the device.
- `foregroundColor`: The foreground color for the element.
- `alignment`: The alignment for the text contained within the element.

## See Also

- [func makeAttributedString(font: UIFont) -> NSAttributedString](tvtextelement/makeattributedstring(font:).md)
  Provides an attributed string for a given font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement/makeattributedstring(font:foregroundcolor:textalignment:))*