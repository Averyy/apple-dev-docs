# extractConnection()

**Framework**: Network  
**Kind**: method

Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func extractConnection() -> NWConnection?
```

## See Also

- [func reply(content: Data?, message: NWConnectionGroup.Message)](nwconnectiongroup/message/reply(content:message:).md)
  Sends a reply to the specific endpoint that originates a group message you receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/message/extractconnection())*