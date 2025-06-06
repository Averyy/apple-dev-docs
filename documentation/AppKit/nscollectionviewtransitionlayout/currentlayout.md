# currentLayout

**Framework**: AppKit  
**Kind**: property

The collection view’s current layout object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var currentLayout: NSCollectionViewLayout { get }
```

#### Discussion

Use this object to retrieve the initial layout attributes for elements of the collection view. If the transition is ultimately cancelled, the collection view animates its items back to the attributes provided by this object.

## See Also

- [var nextLayout: NSCollectionViewLayout](nscollectionviewtransitionlayout/nextlayout.md)
  The collection view’s new layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/currentlayout)*