# WKInterfaceObjectRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- watchOS 6.0+

## Declaration

```swift
typealias Context = WKInterfaceObjectRepresentableContext<Self>
```

## See Also

### Creating and updating the interface object
- [func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType](./makewkinterfaceobject%28context%29.md)
  Creates a WatchKit interface object and configures its initial state.
- [func updateWKInterfaceObject(Self.WKInterfaceObjectType, context: Self.Context)](./updatewkinterfaceobject%28_,context%29.md)
  Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/context)*