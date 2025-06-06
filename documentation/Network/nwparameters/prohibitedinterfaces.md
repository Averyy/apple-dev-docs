# prohibitedInterfaces

**Framework**: Network  
**Kind**: property

A list of specific interfaces that connections and listeners will not use.

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
final var prohibitedInterfaces: [NWInterface]? { get set }
```

## See Also

- [var requiredInterfaceType: NWInterface.InterfaceType](nwparameters/requiredinterfacetype.md)
  An interface type to require on connections and listeners.
- [var requiredInterface: NWInterface?](nwparameters/requiredinterface.md)
  A specific interface to require on connections, listeners, and browsers.
- [var requiredLocalEndpoint: NWEndpoint?](nwparameters/requiredlocalendpoint.md)
  A specific local IP address and port to use for connections and listeners.
- [var prohibitConstrainedPaths: Bool](nwparameters/prohibitconstrainedpaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [var prohibitExpensivePaths: Bool](nwparameters/prohibitexpensivepaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [var prohibitedInterfaceTypes: [NWInterface.InterfaceType]?](nwparameters/prohibitedinterfacetypes.md)
  A list of interface types that connections, listeners, and browsers will not use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/prohibitedinterfaces)*