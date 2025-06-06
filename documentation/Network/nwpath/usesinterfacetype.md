# usesInterfaceType(_:)

**Framework**: Network  
**Kind**: method

Checks if connections using the path may send traffic over a specific interface type.

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
func usesInterfaceType(_ type: NWInterface.InterfaceType) -> Bool
```

#### Discussion

Paths can use interface types by directly routing over an interface, routing through a tunnel that goes over a physical interface, or being eligble to use multiple interfaces directly.

## See Also

- [let availableInterfaces: [NWInterface]](nwpath/availableinterfaces.md)
  A list of all interfaces available to the path, in order of preference.
- [var gateways: [NWEndpoint]](nwpath/gateways.md)
  A list of gateways configured on the interfaces available to a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/usesinterfacetype(_:))*