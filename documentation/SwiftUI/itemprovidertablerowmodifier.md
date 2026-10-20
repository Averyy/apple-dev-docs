# ItemProviderTableRowModifier

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [var body: some _TableRowContentModifier](./itemprovidertablerowmodifier/body-swift.property.md)
### Type Aliases
- [ItemProviderTableRowModifier.Body](./itemprovidertablerowmodifier/body-swift.typealias.md)

## See Also

### Managing interaction
- [func draggable<T>(@autoclosure () -> T) -> some TableRowContent<Self.TableRowValue>
](./tablerowcontent/draggable%28_%29.md)
  Activates this row as the source of a drag and drop operation.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TableRowContent<Self.TableRowValue>
](./tablerowcontent/dropdestination%28for,action%29.md)
  Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onHover(perform: (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
](./tablerowcontent/onhover%28perform%29.md)
  Adds an action to perform when the pointer moves onto or away from the entire row.
- [func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>](./tablerowcontent/itemprovider%28_%29.md)
  Provides a closure that vends the drag representation for a particular data element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/itemprovidertablerowmodifier)*