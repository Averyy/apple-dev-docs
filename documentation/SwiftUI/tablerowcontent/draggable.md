# draggable(_:)

**Framework**: SwiftUI  
**Kind**: method

Activates this row as the source of a drag and drop operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some TableRowContent<Self.TableRowValue> where T : Transferable
```

#### Return Value

A row that activates this row as the source of a drag and drop operation.

#### Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this row.

## Parameters

- `payload`: A closure that returns a single   instance or a value conforming to   that   represents the draggable data from this view.

## See Also

- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/dropdestination(for:action:).md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/onhover(perform:).md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](tablerowcontent/itemprovider(_:).md)
  Provides a closure that vends the drag representation for a particular data element.
- [struct ItemProviderTableRowModifier](itemprovidertablerowmodifier.md)
  A table row modifier that associates an item provider with some base row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/draggable(_:))*