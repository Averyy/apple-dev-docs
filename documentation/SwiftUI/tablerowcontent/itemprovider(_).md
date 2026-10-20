# itemProvider(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Provides a closure that vends the drag representation for a particular data element.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func itemProvider(_ action: (() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>
```

## See Also

### Managing interaction
- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](./draggable%28_%29.md)
  Activates this row as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](./dropdestination%28for,action%29.md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](./onhover%28perform%29.md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [struct ItemProviderTableRowModifier](../itemprovidertablerowmodifier.md)
  A table row modifier that associates an item provider with some base row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/itemprovider(_:))*