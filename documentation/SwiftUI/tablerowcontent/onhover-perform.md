# onHover(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the pointer moves onto or away from the entire row.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func onHover(perform action: @escaping (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
```

## See Also

- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/draggable(_:).md)
  Activates this row as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/dropdestination(for:action:).md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](tablerowcontent/itemprovider(_:).md)
  Provides a closure that vends the drag representation for a particular data element.
- [struct ItemProviderTableRowModifier](itemprovidertablerowmodifier.md)
  A table row modifier that associates an item provider with some base row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/onhover(perform:))*