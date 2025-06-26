# StartCellularConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: struct

Struct representing a request to dial a conversation using the default calling application

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct StartCellularConversationAction
```

## Topics

### Operators
- [static func == (StartCellularConversationAction, StartCellularConversationAction) -> Bool](startcellularconversationaction/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](startcellularconversationaction/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(handle: Handle, cellularService: CellularService?)](startcellularconversationaction/init(handle:cellularservice:).md)
  Initializer for a dial request which accepts a handle to dial and an account to use to dial with. If no account is provided then the system will choose an account to dial with or fail to dial
- [init(recentConversation: ConversationHistoryManager.RecentConversation)](startcellularconversationaction/init(recentconversation:).md)
### Instance Properties
- [var hashValue: Int](startcellularconversationaction/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](startcellularconversationaction/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](startcellularconversationaction/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](startcellularconversationaction/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction)*