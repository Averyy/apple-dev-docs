# filterBrowsers

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates that the system applies the filter to flows of network data originated from WebKit browser objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: filterBrowsers is not supported on macOS

## Declaration

```swift
var filterBrowsers: Bool { get set }
```

```objc
@property BOOL filterBrowsers;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring filter behavior
- [var filterSockets: Bool](./filtersockets.md)
  A Boolean value that indicates that the system applies the filter to flows of network data originated from sockets.
- [var filterPackets: Bool](./filterpackets.md)
  A Boolean value that indicates that the system applies the filter to packets of network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/filterbrowsers)*