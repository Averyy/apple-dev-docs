# DragConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The behavior of the drag, proposed by the dragging source.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DragConfiguration
```

## Topics

### Structures
- [DragConfiguration.OperationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.struct.md)
  Describes the suggested drag operations to other applications.
- [DragConfiguration.OperationsWithinApp](dragconfiguration/operationswithinapp-swift.struct.md)
  Describes the drag operations suggested to destinations within the app.
### Initializers
- [init(allowMove: Bool)](dragconfiguration/init(allowmove:).md)
  Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.
- [init(allowMove: Bool, allowDelete: Bool)](dragconfiguration/init(allowmove:allowdelete:).md)
  Creates a drag configuration that can support drag-to-move and drag-to-delete in addition to drag-to-copy.
- [init(operationsWithinApp: DragConfiguration.OperationsWithinApp, operationsOutsideApp: DragConfiguration.OperationsOutsideApp)](dragconfiguration/init(operationswithinapp:operationsoutsideapp:).md)
  Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.
### Instance Properties
- [var operationsOutsideApp: DragConfiguration.OperationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.property.md)
  The operations suggested by the drag source for drags to other applications.
- [var operationsWithinApp: DragConfiguration.OperationsWithinApp](dragconfiguration/operationswithinapp-swift.property.md)
  The operations suggested by the drag source for drags within the application.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)

## See Also

- [struct DropConfiguration](dropconfiguration.md)
  Describes the behavior of the drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragconfiguration)*