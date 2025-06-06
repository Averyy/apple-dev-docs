# nextFocusedIndexPath

**Framework**: UIKit  
**Kind**: property

The index path of the collection view cell that’s receiving the focus.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nextFocusedIndexPath: IndexPath? { get }
```

#### Discussion

This property contains the index path only when the view receiving focus belongs to a cell of the collection view. If focus is moving to a view outside of the collection view and its cells, this property is `nil`.

## See Also

- [var previouslyFocusedIndexPath: IndexPath?](uicollectionviewfocusupdatecontext/previouslyfocusedindexpath.md)
  The index path of the collection view cell that previously had the focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/nextfocusedindexpath)*