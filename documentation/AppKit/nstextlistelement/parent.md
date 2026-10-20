# parent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A text list element that refers to the enclosing text list element.

**Availability**:
- macOS 13.0+

## Declaration

```swift
weak var parent: NSTextListElement? { get }
```

```objc
@property (weak, readonly, nullable) NSTextListElement * parentElement;
```

## See Also

### Accessing the text elements
- [var textList: NSTextList](./textlist.md)
  The value that represents the text list.
- [var childElements: [NSTextListElement]](./childelements.md)
  An array that contains child text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement/parent)*