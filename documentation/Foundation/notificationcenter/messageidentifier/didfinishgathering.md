# didFinishGathering

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a metadata query that finished its initial result gathering.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var didFinishGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidFinishGatheringMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidFinishGatheringMessage>`.

#### Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`NSMetadataQuery.DidStartGatheringMessage`](../../nsmetadataquery/didstartgatheringmessage.md).

## See Also

### Identifying metadata query messages
- [static var didStartGathering: NotificationCenter.BaseMessageIdentifier<NSMetadataQuery.DidStartGatheringMessage>](./didstartgathering.md)
  An identifier for a message about a metadata query that is starting its initial result gathering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didfinishgathering)*