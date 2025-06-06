# attributedString(for:)

**Framework**: UIKit  
**Kind**: method

Returns a new attributed string for the text element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func attributedString(for textElement: NSTextElement) -> NSAttributedString?
```

#### Return Value

An [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), or `nil`.

#### Discussion

Returns `nil` if the method can’t map `textElement` to an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString).

## Parameters

- `textElement`: The   to map into an attributed string.

## See Also

- [func textElement(for: NSAttributedString) -> NSTextElement?](nstextcontentstorage/textelement(for:).md)
  Returns the text element corresponding to object’s attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/attributedstring(for:))*