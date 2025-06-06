# filterBrowsers

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates that the system applies the filter to flows of network data originated from WebKit browser objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var filterBrowsers: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var filterSockets: Bool](nefilterproviderconfiguration/filtersockets.md)
  A Boolean value that indicates that the system applies the filter to flows of network data originated from sockets.
- [var filterPackets: Bool](nefilterproviderconfiguration/filterpackets.md)
  A Boolean value that indicates that the system applies the filter to packets of network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/filterbrowsers)*