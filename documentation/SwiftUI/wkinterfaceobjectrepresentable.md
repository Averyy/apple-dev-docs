# WKInterfaceObjectRepresentable

**Framework**: SwiftUI  
**Kind**: protocol

A view that represents a WatchKit interface object.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol WKInterfaceObjectRepresentable : View where Self.Body == Never
```

#### Overview

Use a `WKInterfaceObjectRepresentable` instance to create and manage a [`WKInterfaceObject`](https://developer.apple.com/documentation/WatchKit/WKInterfaceObject) in your SwiftUI interface. Adopt this protocol in one of your app’s custom instances, and use its methods to create, update, and tear down your interface object. The creation and update processes parallel the behavior of SwiftUI views, and you use them to configure your interface object with your app’s current state information. Use the teardown process to remove your interface object cleanly from your SwiftUI. For example, you might use the teardown process to notify other parts of your app that the interface object is disappearing.

To add your interface object into your SwiftUI interface, create your `WKInterfaceObjectRepresentable` instance and add it to your SwiftUI interface. The system calls the methods of your representable instance at appropriate times to create and update the interface object.

The system doesn’t automatically communicate changes occurring within your interface object to other parts of your SwiftUI interface. When you want your interface object to coordinate with other SwiftUI views, you must provide a [`Coordinator`](wkinterfaceobjectrepresentable/coordinator.md) instance to facilitate those interactions. For example, you use a coordinator to forward target-action and delegate messages from your interface object to any SwiftUI views.

## Topics

### Creating and updating the interface object
- [func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType](wkinterfaceobjectrepresentable/makewkinterfaceobject(context:).md)
  Creates a WatchKit interface object and configures its initial state.
- [func updateWKInterfaceObject(Self.WKInterfaceObjectType, context: Self.Context)](wkinterfaceobjectrepresentable/updatewkinterfaceobject(_:context:).md)
  Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.
- [WKInterfaceObjectRepresentable.Context](wkinterfaceobjectrepresentable/context.md)
### Cleaning up the interface object
- [static func dismantleWKInterfaceObject(Self.WKInterfaceObjectType, coordinator: Self.Coordinator)](wkinterfaceobjectrepresentable/dismantlewkinterfaceobject(_:coordinator:).md)
  Cleans up the presented WatchKit interface object (and its coordinator) in anticipation of their removal.
### Providing a custom coordinator object
- [func makeCoordinator() -> Self.Coordinator](wkinterfaceobjectrepresentable/makecoordinator.md)
  Creates the custom instance that you use to communicate changes from your interface object to other parts of your SwiftUI interface.
- [associatedtype Coordinator = Void](wkinterfaceobjectrepresentable/coordinator.md)
  A type to coordinate with the WatchKit interface object.
- [associatedtype WKInterfaceObjectType : WKInterfaceObject](wkinterfaceobjectrepresentable/wkinterfaceobjecttype.md)
  The type of WatchKit interface object to be presented.

## Relationships

### Inherits From
- [View](view.md)

## See Also

- [struct WKInterfaceObjectRepresentableContext](wkinterfaceobjectrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your WatchKit interface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable)*