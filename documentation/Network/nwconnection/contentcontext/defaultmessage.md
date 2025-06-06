# defaultMessage

**Framework**: Network  
**Kind**: property

A static context representing a message with default properties.

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
static let defaultMessage: NWConnection.ContentContext
```

#### Discussion

You should use this context for sending content unless there is a reason to override some values.

## See Also

- [static let finalMessage: NWConnection.ContentContext](nwconnection/contentcontext/finalmessage.md)
  A static context that’s marked as the final message in a connection.
- [static let defaultStream: NWConnection.ContentContext](nwconnection/contentcontext/defaultstream.md)
  A static context representing the total stream of bytes on a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext/defaultmessage)*