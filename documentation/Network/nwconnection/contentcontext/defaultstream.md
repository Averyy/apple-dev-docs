# defaultStream

**Framework**: Network  
**Kind**: property  
**Role**: Type Property

A static context representing the total stream of bytes on a connection.

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
static let defaultStream: NWConnection.ContentContext
```

#### Discussion

Once this context is used for sending, and the send is marked as complete, no more data can be sent on the connection.

## See Also

### Using Constant Send Contexts
- [static let defaultMessage: NWConnection.ContentContext](./defaultmessage.md)
  A static context representing a message with default properties.
- [static let finalMessage: NWConnection.ContentContext](./finalmessage.md)
  A static context that’s marked as the final message in a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/contentcontext/defaultstream)*