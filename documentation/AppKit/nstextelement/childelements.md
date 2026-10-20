# childElements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of zero or more child text elements.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var childElements: [NSTextElement] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSTextElement *> * childElements;
```

## See Also

### Accessing text elements
- [var isRepresentedElement: Bool](./isrepresentedelement.md)
  A Boolean value that indicates whether this element is in the text layout.
- [var parent: NSTextElement?](./parent.md)
  A value that represents the parent element if this text element is a child of an enclosing element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelement/childelements)*