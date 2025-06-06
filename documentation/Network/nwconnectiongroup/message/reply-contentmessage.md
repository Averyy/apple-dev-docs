# reply(content:message:)

**Framework**: Network  
**Kind**: method

Sends a reply to the specific endpoint that originates a group message you receive.

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
func reply(content: Data?, message: NWConnectionGroup.Message = .default)
```

## See Also

- [func extractConnection() -> NWConnection?](nwconnectiongroup/message/extractconnection.md)
  Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/message/reply(content:message:))*