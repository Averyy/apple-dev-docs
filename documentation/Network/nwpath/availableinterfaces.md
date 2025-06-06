# availableInterfaces

**Framework**: Network  
**Kind**: property

A list of all interfaces available to the path, in order of preference.

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
let availableInterfaces: [NWInterface]
```

## See Also

- [func usesInterfaceType(NWInterface.InterfaceType) -> Bool](nwpath/usesinterfacetype(_:).md)
  Checks if connections using the path may send traffic over a specific interface type.
- [var gateways: [NWEndpoint]](nwpath/gateways.md)
  A list of gateways configured on the interfaces available to a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/availableinterfaces)*