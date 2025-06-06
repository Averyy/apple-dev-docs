# updateWKInterfaceObject(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateWKInterfaceObject(_ wkInterfaceObject: Self.WKInterfaceObjectType, context: Self.Context)
```

#### Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding interface object. Use this method to update the configuration of your object to match the new state information provided in the `context` parameter.

## Parameters

- `wkInterfaceObject`: Your custom interface object.
- `context`: A context structure containing information about the current   state of the system.

## See Also

- [func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType](wkinterfaceobjectrepresentable/makewkinterfaceobject(context:).md)
  Creates a WatchKit interface object and configures its initial state.
- [WKInterfaceObjectRepresentable.Context](wkinterfaceobjectrepresentable/context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/updatewkinterfaceobject(_:context:))*