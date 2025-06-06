# status

**Framework**: Network Extension  
**Kind**: property

The evaluated status of the network path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var status: NWPathStatus { get }
```

#### Discussion

The status of a path indicates whether or not the process is able to make connection attempts to any, or a specific, network endpoint. A satisfied status does not guarantee that a connection will be successful, but it does ensure that there is some interface over which an attempt can be made.

## See Also

- [enum NWPathStatus](nwpathstatus.md)
- [var isExpensive: Bool](nwpath/isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.
- [var isConstrained: Bool](nwpath/isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/status)*