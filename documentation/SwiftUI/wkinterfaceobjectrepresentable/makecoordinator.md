# makeCoordinator()

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the custom instance that you use to communicate changes from your interface object to other parts of your SwiftUI interface.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator() -> Self.Coordinator
```

#### Discussion

Implement this method if changes to your interface object might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your interface object doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [`makeWKInterfaceObject(context:)`](wkinterfaceobjectrepresentable/makewkinterfaceobject(context:).md) method. The system provides your coordinator either directly or as part of a context structure when calling the other methods of your representable instance.

## See Also

- [associatedtype Coordinator = Void](wkinterfaceobjectrepresentable/coordinator.md)
  A type to coordinate with the WatchKit interface object.
- [associatedtype WKInterfaceObjectType : WKInterfaceObject](wkinterfaceobjectrepresentable/wkinterfaceobjecttype.md)
  The type of WatchKit interface object to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/makecoordinator())*