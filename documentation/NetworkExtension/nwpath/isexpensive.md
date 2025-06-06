# isExpensive

**Framework**: Network Extension  
**Kind**: property

A Boolean that indicates whether or not the path uses an expensive interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isExpensive: Bool { get }
```

#### Discussion

Returns YES is the path uses an interface that is considered expensive, such as when using a cellular data plan.

## See Also

- [var status: NWPathStatus](nwpath/status.md)
  The evaluated status of the network path.
- [enum NWPathStatus](nwpathstatus.md)
- [var isConstrained: Bool](nwpath/isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/isexpensive)*