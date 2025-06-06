# makeAttributedString(font:)

**Framework**: TVMLKit  
**Kind**: method

Provides an attributed string for a given font.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func makeAttributedString(font: UIFont) -> NSAttributedString
```

#### Return Value

An [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) object with the supplied font.

#### Discussion

Supply a font to this method to get the [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) representation of the text contained within an element.

## Parameters

- `font`: The font used for the attributed string. This can be any available font on the device.

## See Also

- [func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment: NSTextAlignment) -> NSAttributedString](tvtextelement/makeattributedstring(font:foregroundcolor:textalignment:).md)
  Convenience method for configuring an attributed string given the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement/makeattributedstring(font:))*