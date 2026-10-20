# init(requiredInterfaceType:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a path monitor to observe a specific interface type.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(requiredInterfaceType: NWInterface.InterfaceType)
```

## See Also

### Creating Path Monitors
- [init()](./init%28%29.md)
  Initializes a path monitor to observe all available interface types.
- [init(prohibitedInterfaceTypes: [NWInterface.InterfaceType])](./init%28prohibitedinterfacetypes%29.md)
  Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts monitoring path changes, and sets a queue on which to deliver path events.
- [var queue: DispatchQueue?](./queue.md)
  The queue on which path events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpathmonitor/init(requiredinterfacetype:))*