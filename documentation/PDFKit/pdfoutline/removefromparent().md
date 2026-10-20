# removeFromParent()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Removes the outline object from its parent (does nothing if outline object is the root outline object).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromParent()
```

```objc
- (void) removeFromParent;
```

## See Also

### Related Documentation
- [var parent: PDFOutline?](./parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
### Changing an Outline Hierarchy
- [func insertChild(PDFOutline, at: Int)](./insertchild%28_,at%29.md)
  Inserts the specified outline object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/removefromparent())*