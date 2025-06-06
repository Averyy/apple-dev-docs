# currentPath

**Framework**: Network  
**Kind**: property

The network path the connection is using.

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
final var currentPath: NWPath? { get }
```

## See Also

- [var pathUpdateHandler: ((NWPath) -> Void)?](nwconnection/pathupdatehandler.md)
  A handler that receives network path updates.
- [var viabilityUpdateHandler: ((Bool) -> Void)?](nwconnection/viabilityupdatehandler.md)
  A handler that receives updates when data can be sent and received.
- [var betterPathUpdateHandler: ((Bool) -> Void)?](nwconnection/betterpathupdatehandler.md)
  A handler that receives updates when an alternative network path is preferred over the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/currentpath)*