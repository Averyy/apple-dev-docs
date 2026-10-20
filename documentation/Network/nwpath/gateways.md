# gateways

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A list of gateways configured on the interfaces available to a path.

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
var gateways: [NWEndpoint] { get }
```

## See Also

### Inspecting Interfaces
- [func usesInterfaceType(NWInterface.InterfaceType) -> Bool](./usesinterfacetype%28_%29.md)
  Checks if connections using the path may send traffic over a specific interface type.
- [let availableInterfaces: [NWInterface]](./availableinterfaces.md)
  A list of all interfaces available to the path, in order of preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/gateways)*