# DragConfiguration.OperationsOutsideApp

**Framework**: SwiftUI  
**Kind**: struct

Describes the suggested drag operations to other applications.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct OperationsOutsideApp
```

#### Overview

To create a default configuration, initialize it without parameters.

On iOS, the default behavior is to disallow drag outside the application. On macOS—support drag-to-copy to destinations both within the application and to other apps.

In addition to `copy`, add `move` operation support by specifying that in the initializer:

```swift
   struct DraggableBookView: View {
       var id: UUID

       var body: some View {
           BookView()
               .draggable(Book(id: id))
               .dragConfiguration(makeConfiguration())
       }

       func makeConfiguration() -> DragConfiguration {
           let operations = OperationsOutsideApp(
               allowCopy: true, allowMove: true
           )
           return DragConfiguration(operationsOutsideApp: operations)
       }
   }
```

In the example above, an application provides operations that will be suggested to other applications. Drags to destinations within the app will use the default behavior: suggest operation `copy` to drag destinations.

## Topics

### Initializers
- [init(allowCopy: Bool)](dragconfiguration/operationsoutsideapp-swift.struct/init(allowcopy:).md)
  Creates a value that describes the operations allowed for drags to other applications.
- [init(allowCopy: Bool, allowMove: Bool, allowDelete: Bool)](dragconfiguration/operationsoutsideapp-swift.struct/init(allowcopy:allowmove:allowdelete:).md)
  Creates a value that describes the operations allowed for drags to other applications.
### Instance Properties
- [var allowAlias: Bool](dragconfiguration/operationsoutsideapp-swift.struct/allowalias.md)
  A Boolean value indicating if the drag operation supports creating aliases to the dropped items.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.struct)*