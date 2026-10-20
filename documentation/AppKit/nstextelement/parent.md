# parent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the parent element if this text element is a child of an enclosing element.

**Availability**:
- macOS 13.0+

## Declaration

```swift
weak var parent: NSTextElement? { get }
```

```objc
@property (weak, readonly, nullable) NSTextElement * parentElement;
```

## See Also

### Accessing text elements
- [var isRepresentedElement: Bool](./isrepresentedelement.md)
  A Boolean value that indicates whether this element is in the text layout.
- [var childElements: [NSTextElement]](./childelements.md)
  An array of zero or more child text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelement/parent)*