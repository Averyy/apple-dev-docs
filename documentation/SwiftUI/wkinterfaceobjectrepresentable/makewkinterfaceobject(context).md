# makeWKInterfaceObject(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a WatchKit interface object and configures its initial state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType
```

## Return Value

Your interface object configured with the provided information.

## Discussion

You must implement this method and use it to create your interface object. Configure the object using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your interface object for the first time. For all subsequent updates, the system calls the [`updateWKInterfaceObject(_:context:)`](./updatewkinterfaceobject%28_,context%29.md) method.

## Parameters

- `context`: A context structure containing information about the current state of the system.

## See Also

### Creating and updating the interface object
- [func updateWKInterfaceObject(Self.WKInterfaceObjectType, context: Self.Context)](./updatewkinterfaceobject%28_,context%29.md)
  Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.
- [WKInterfaceObjectRepresentable.Context](./context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/makewkinterfaceobject(context:))*