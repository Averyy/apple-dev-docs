# prohibitConstrainedPaths

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final var prohibitConstrainedPaths: Bool { get set }
```

## See Also

### Selecting Paths
- [var requiredInterfaceType: NWInterface.InterfaceType](./requiredinterfacetype.md)
  An interface type to require on connections and listeners.
- [var requiredInterface: NWInterface?](./requiredinterface.md)
  A specific interface to require on connections, listeners, and browsers.
- [var requiredLocalEndpoint: NWEndpoint?](./requiredlocalendpoint.md)
  A specific local IP address and port to use for connections and listeners.
- [var prohibitExpensivePaths: Bool](./prohibitexpensivepaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [var prohibitedInterfaceTypes: [NWInterface.InterfaceType]?](./prohibitedinterfacetypes.md)
  A list of interface types that connections, listeners, and browsers will not use.
- [var prohibitedInterfaces: [NWInterface]?](./prohibitedinterfaces.md)
  A list of specific interfaces that connections and listeners will not use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/prohibitconstrainedpaths)*