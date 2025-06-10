# DragConfiguration.OperationsWithinApp

**Framework**: SwiftUI  
**Kind**: struct

Describes the drag operations suggested to destinations within the app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct OperationsWithinApp
```

#### Overview

To create a default configuration, initialize it without parameters.

On iOS, the default behavior is to allow drag-to-copy within the application. On macOS, the default configuration is to support drag-to-copy to destinations both within the application and to other apps.

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
           let operations = OperationsWithinApp(allowMove: true)
           return DragConfiguration(operationsWithinApp: operations)
       }
   }
```

In the example above, an application provides operations that will be suggested to destinations within the app. Drags to other apps will use the default behavior: suggest operation `copy` to drag destinations on macOS, and forbid drags on iOS.

## Topics

### Initializers
- [init(allowCopy: Bool, allowMove: Bool, allowDelete: Bool)](dragconfiguration/operationswithinapp-swift.struct/init(allowcopy:allowmove:allowdelete:).md)
  Creates a value that describes the operations allowed for drags that end within the application.
- [init(allowMove: Bool)](dragconfiguration/operationswithinapp-swift.struct/init(allowmove:).md)
  Creates a value that describes the operations allowed for drags that end within the application. Copy operation is always allowed.
### Instance Properties
- [var allowAlias: Bool](dragconfiguration/operationswithinapp-swift.struct/allowalias.md)
  A Boolean value indicating if the drag operation supports creating aliases to the dropped items.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragconfiguration/operationswithinapp-swift.struct)*