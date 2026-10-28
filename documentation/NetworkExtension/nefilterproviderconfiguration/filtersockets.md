# filterSockets

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates that the system applies the filter to flows of network data originated from sockets.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var filterSockets: Bool { get set }
```

```objc
@property BOOL filterSockets;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring filter behavior
- [var filterBrowsers: Bool](./filterbrowsers.md)
  A Boolean value that indicates that the system applies the filter to flows of network data originated from WebKit browser objects.
- [var filterPackets: Bool](./filterpackets.md)
  A Boolean value that indicates that the system applies the filter to packets of network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/filtersockets)*