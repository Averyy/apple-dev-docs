# nextLayout

**Framework**: AppKit  
**Kind**: property

The collection view’s new layout object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var nextLayout: NSCollectionViewLayout { get }
```

#### Discussion

Use this object to retrieve the final layout attributes for elements of the collection view. If the transition completes as expected, the collection view animates its items to the attributes provided by this object.

## See Also

- [var currentLayout: NSCollectionViewLayout](nscollectionviewtransitionlayout/currentlayout.md)
  The collection view’s current layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/nextlayout)*