# DropInfo

**Framework**: SwiftUI  
**Kind**: struct

The current state of a drop.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct DropInfo
```

## Topics

### Getting the drop location
- [var location: CGPoint](dropinfo/location.md)
  The location of the drag in the coordinate space of the drop view.
### Checking for items
- [func hasItemsConforming(to: [UTType]) -> Bool](dropinfo/hasitemsconforming(to:)-47irh.md)
  Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [func itemProviders(for: [UTType]) -> [NSItemProvider]](dropinfo/itemproviders(for:)-93409.md)
  Finds item providers that conform to at least one of the specified uniform type identifiers.
### Deprecated symbols
- [func hasItemsConforming(to: [String]) -> Bool](dropinfo/hasitemsconforming(to:)-4qeez.md)
  Returns whether at least one item conforms to at least one of the specified uniform type identifiers.
- [func itemProviders(for: [String]) -> [NSItemProvider]](dropinfo/itemproviders(for:)-b6fo.md)
  Returns an array of items that each conform to at least one of the specified uniform type identifiers.
### Instance Methods
- [func hasItemsConforming(to:)](dropinfo/hasitemsconforming(to:).md)
  Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [func itemProviders(for:)](dropinfo/itemproviders(for:).md)
  Finds item providers that conform to at least one of the specified uniform type identifiers.

## See Also

- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](view/ondrop(of:delegate:).md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropinfo)*