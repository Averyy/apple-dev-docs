# NWParameters.MultipathServiceType.handover

**Framework**: Network  
**Kind**: case  
**Role**: Case

Enable multipath, but only use other interfaces when the primary interface is lost.

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
case handover
```

## See Also

### Multipath Service Types
- [NWParameters.MultipathServiceType.disabled](./disabled.md)
  Disable multipath.
- [NWParameters.MultipathServiceType.interactive](./interactive.md)
  Enable multipath to use other interfaces when the primary interface encounters loss or delay.
- [NWParameters.MultipathServiceType.aggregate](./aggregate.md)
  Enable multipath to maximize bandwidth across multiple interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/multipathservicetype-swift.enum/handover)*