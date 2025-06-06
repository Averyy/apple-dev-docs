# prohibitExpensivePaths

**Framework**: Network  
**Kind**: property

A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.

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
final var prohibitExpensivePaths: Bool { get set }
```

#### Discussion

To test the behavior of this property, you can override the device’s current values for cellular and Wi-Fi cost in Settings > Developer > Network Override.

> 💡 **Tip**:  Prefer basing your app’s policy logic around the [`prohibitConstrainedPaths`](nwparameters/prohibitconstrainedpaths.md) property rather than this one. People using your app can use the “Low Data Mode” setting to set the constrained status, and thereby choose to use a potentially expensive network.

 Prefer basing your app’s policy logic around the [`prohibitConstrainedPaths`](nwparameters/prohibitconstrainedpaths.md) property rather than this one. People using your app can use the “Low Data Mode” setting to set the constrained status, and thereby choose to use a potentially expensive network.

## See Also

- [var requiredInterfaceType: NWInterface.InterfaceType](nwparameters/requiredinterfacetype.md)
  An interface type to require on connections and listeners.
- [var requiredInterface: NWInterface?](nwparameters/requiredinterface.md)
  A specific interface to require on connections, listeners, and browsers.
- [var requiredLocalEndpoint: NWEndpoint?](nwparameters/requiredlocalendpoint.md)
  A specific local IP address and port to use for connections and listeners.
- [var prohibitConstrainedPaths: Bool](nwparameters/prohibitconstrainedpaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [var prohibitedInterfaceTypes: [NWInterface.InterfaceType]?](nwparameters/prohibitedinterfacetypes.md)
  A list of interface types that connections, listeners, and browsers will not use.
- [var prohibitedInterfaces: [NWInterface]?](nwparameters/prohibitedinterfaces.md)
  A list of specific interfaces that connections and listeners will not use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/prohibitexpensivepaths)*