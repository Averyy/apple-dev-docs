# ItemProviderTableRowModifier

**Framework**: SwiftUI  
**Kind**: struct

A table row modifier that associates an item provider with some base row content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ItemProviderTableRowModifier
```

## Topics

### Instance Properties
- [var body: some _TableRowContentModifier](itemprovidertablerowmodifier/body-swift.property.md)
### Type Aliases
- [ItemProviderTableRowModifier.Body](itemprovidertablerowmodifier/body-swift.typealias.md)

## See Also

- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/draggable(_:).md)
  Activates this row as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/dropdestination(for:action:).md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/onhover(perform:).md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](tablerowcontent/itemprovider(_:).md)
  Provides a closure that vends the drag representation for a particular data element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/itemprovidertablerowmodifier)*