# textElement(for:)

**Framework**: UIKit  
**Kind**: method

Returns the text element corresponding to object’s attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textElement(for attributedString: NSAttributedString) -> NSTextElement?
```

#### Return Value

An [`NSTextElement`](nstextelement.md), or `nil`.

#### Discussion

Returns `nil` when `attributedString` contains attributes not mappable to [`NSTextElement`](nstextelement.md).

## Parameters

- `attributedString`: The attributed string to map into an  .

## See Also

- [func attributedString(for: NSTextElement) -> NSAttributedString?](nstextcontentstorage/attributedstring(for:).md)
  Returns a new attributed string for the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/textelement(for:))*