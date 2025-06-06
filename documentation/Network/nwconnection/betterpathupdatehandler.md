# betterPathUpdateHandler

**Framework**: Network  
**Kind**: property

A handler that receives updates when an alternative network path is preferred over the current path.

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
@preconcurrency
final var betterPathUpdateHandler: ((Bool) -> Void)? { get set }
```

#### Discussion

Better path events are an indication that a more preferable network path is available. If you can migrate your work to a new connection, try establishing a new connection. Once that new connection is ready, cancel the original connection.

## See Also

- [var currentPath: NWPath?](nwconnection/currentpath.md)
  The network path the connection is using.
- [var pathUpdateHandler: ((NWPath) -> Void)?](nwconnection/pathupdatehandler.md)
  A handler that receives network path updates.
- [var viabilityUpdateHandler: ((Bool) -> Void)?](nwconnection/viabilityupdatehandler.md)
  A handler that receives updates when data can be sent and received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/betterpathupdatehandler)*