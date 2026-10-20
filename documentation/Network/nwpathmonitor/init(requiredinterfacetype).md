# init(requiredInterfaceType:)

**Framework**: Network  
**Kind**: init

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

- [init()](nwpathmonitor/init.md)
  Initializes a path monitor to observe all available interface types.
- [init(prohibitedInterfaceTypes: [NWInterface.InterfaceType])](nwpathmonitor/init(prohibitedinterfacetypes:).md)
  Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [func start(queue: DispatchQueue)](nwpathmonitor/start(queue:).md)
  Starts monitoring path changes, and sets a queue on which to deliver path events.
- [var queue: DispatchQueue?](nwpathmonitor/queue.md)
  The queue on which path events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpathmonitor/init(requiredinterfacetype:))*