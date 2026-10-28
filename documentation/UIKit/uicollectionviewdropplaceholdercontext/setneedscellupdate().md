# setNeedsCellUpdate()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates the contents of the placeholder cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setNeedsCellUpdate()
```

```objc
- (void) setNeedsCellUpdate;
```

## Discussion

Call this method when you want to update the contents of the placeholder cell. When you call this method, UIKit calls the update handler that you originally passed to the `drop(_:toPlaceholderInsertedAt:withReuseIdentifier:cellUpdateHandler:)` method when creating the cell.

## See Also

### Updating the Placeholder Cell
- [func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool](./commitinsertion%28datasourceupdates%29.md)
  Exchanges the placeholder cell for a cell with the final content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext/setneedscellupdate())*