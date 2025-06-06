# dropDestination(for:action:)

**Framework**: SwiftUI  
**Kind**: method

Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Void) -> some TableRowContent<Self.TableRowValue> where T : Transferable
```

#### Return Value

A row that provides a drop destination for a drag operation of the specified type.

## Parameters

- `payloadType`: The expected type of the dropped models.
- `action`: A closure that takes the dropped content and responds   with   if the drop operation was successful; otherwise, return   .

## See Also

- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/draggable(_:).md)
  Activates this row as the source of a drag and drop operation.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](tablerowcontent/onhover(perform:).md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](tablerowcontent/itemprovider(_:).md)
  Provides a closure that vends the drag representation for a particular data element.
- [struct ItemProviderTableRowModifier](itemprovidertablerowmodifier.md)
  A table row modifier that associates an item provider with some base row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/dropdestination(for:action:))*