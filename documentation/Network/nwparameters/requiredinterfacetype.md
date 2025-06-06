# requiredInterfaceType

**Framework**: Network  
**Kind**: property

An interface type to require on connections and listeners.

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
final var requiredInterfaceType: NWInterface.InterfaceType { get set }
```

## See Also

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
- [var prohibitedInterfaces: [NWInterface]?](nwparameters/prohibitedinterfaces.md)
  A list of specific interfaces that connections and listeners will not use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/requiredinterfacetype)*