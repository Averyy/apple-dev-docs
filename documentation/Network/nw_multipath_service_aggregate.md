# nw_multipath_service_aggregate

**Framework**: Network  
**Kind**: var

Enable multipath to maximize bandwidth across multiple interfaces.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var nw_multipath_service_aggregate: nw_multipath_service_t { get }
```

## See Also

- [var nw_multipath_service_disabled: nw_multipath_service_t](nw_multipath_service_disabled.md)
  Disable multipath.
- [var nw_multipath_service_handover: nw_multipath_service_t](nw_multipath_service_handover.md)
  Enable multipath, but only use other interfaces when the primary interface is lost.
- [var nw_multipath_service_interactive: nw_multipath_service_t](nw_multipath_service_interactive.md)
  Enable multipath to use other interfaces when the primary interface encounters loss or delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_multipath_service_aggregate)*