# centerIndexPath

**Framework**: TVUIKit  
**Kind**: property

The index path of the currently centered item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var centerIndexPath: IndexPath? { get }
```

#### Discussion

The `centerIndexPath` property returns the index path of the cell currently centered on the screen. `TVUIKit` calculates the current index path using the current content offset of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout/centerindexpath)*