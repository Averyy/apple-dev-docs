# init(prohibitedInterfaceTypes:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a path monitor to observe interface types that are not explicitly prohibited.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(prohibitedInterfaceTypes: [NWInterface.InterfaceType])
```

## See Also

### Creating Path Monitors
- [init()](./init%28%29.md)
  Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType: NWInterface.InterfaceType)](./init%28requiredinterfacetype%29.md)
  Initializes a path monitor to observe a specific interface type.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts monitoring path changes, and sets a queue on which to deliver path events.
- [var queue: DispatchQueue?](./queue.md)
  The queue on which path events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpathmonitor/init(prohibitedinterfacetypes:))*