# init(identifier:expiration:priority:isFinal:antecedent:metadata:)

**Framework**: Network  
**Kind**: init

Initializes a custom message context you use to send data.

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
override init(identifier: String, expiration: UInt64 = super, priority: Double = super, isFinal: Bool = super, antecedent: NWConnection.ContentContext? = nil, metadata: [NWProtocolMetadata]? = super)
```

## See Also

- [static let `default`: NWConnectionGroup.Message](nwconnectiongroup/message/default.md)
  A static object you use to send a message with default properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/message/init(identifier:expiration:priority:isfinal:antecedent:metadata:))*