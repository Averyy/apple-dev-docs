# clearNonenumeratedImages

**Framework**: AppKit  
**Kind**: property

A constant that indicates the enumeration clears the image components provider for all dragging items that don’t meet the classes and search options criteria.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var clearNonenumeratedImages: NSDraggingItemEnumerationOptions { get }
```

#### Discussion

Specify this option when you enumerate dragging items to hide the drag image for nonvalid items for this destination. The enumeration sets the [`imageComponentsProvider`](nsdraggingitem/imagecomponentsprovider.md) to `nil` for all dragging items that don’t meet the classes and search options criteria.

## See Also

- [static var concurrent: NSDraggingItemEnumerationOptions](nsdraggingitemenumerationoptions/concurrent.md)
  A constant that indicates the enumeration processes dragging items concurrently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions/clearnonenumeratedimages)*