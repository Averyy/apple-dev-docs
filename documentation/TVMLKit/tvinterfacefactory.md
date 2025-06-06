# TVInterfaceFactory

**Framework**: TVMLKit  
**Kind**: class

A factory for the creation of views and view controllers.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVInterfaceFactory
```

#### Overview

The app can extend or override the framework implementation by setting [`extendedInterfaceCreator`](tvinterfacefactory/extendedinterfacecreator.md).

## Topics

### Extending an Interface
- [var extendedInterfaceCreator: (any TVInterfaceCreating)?](tvinterfacefactory/extendedinterfacecreator.md)
  The interface that is being extended.
- [class func shared() -> Self](tvinterfacefactory/shared.md)
  Returns the singleton instance of the interface factory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TVInterfaceCreating](tvinterfacecreating.md)

## See Also

- [class TVViewElement](tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVBrowserViewController](tvbrowserviewcontroller.md)
  A view controller that presents content in a browsable, full-screen format.
- [class TVDocumentViewController](tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory)*