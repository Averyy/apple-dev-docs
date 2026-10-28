# insertChild(_:at:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Inserts the specified outline object at the specified index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func insertChild(_ child: PDFOutline, at index: Int)
```

```objc
- (void) insertChild:(PDFOutline *) child atIndex:(NSUInteger) index;
```

## Discussion

To build a PDF outline hierarchy, use this method to add child outline objects. Before you call this method on a `PDFOutline` object that already has a parent, you should retain the object and call [`removeFromParent()`](./removefromparent%28%29.md) on it first.

## See Also

### Related Documentation
- [func child(at: Int) -> PDFOutline?](./child%28at%29.md)
  Returns the child outline object at the specified index.
### Changing an Outline Hierarchy
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the outline object from its parent (does nothing if outline object is the root outline object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/insertchild(_:at:))*