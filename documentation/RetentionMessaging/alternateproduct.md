# alternateProduct

**Framework**: Retention Messaging API  
**Kind**: dictionary

A switch-plan message and product ID you provide in a real-time response to your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object alternateProduct
```

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

In your [`RealtimeResponseBody`](realtimeresponsebody.md) real-time response, you can choose from mutually exclusive options. Include `alternateProduct` in your response to provide a switch-plan retention message.

Use the product identifier in [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md) to determine the customer’s current subscription. Choose an alternative subscription from the same subscription group.

The message identifier needs to refer to a message that doesn’t include an image and that has a [`messageState`](messagestate.md) of `APPROVED`; otherwise, the retention message fails. For more information about setting up messages, see [`Upload Message`](upload-message.md).

## See Also

- [object message](message.md)
  A message identifier you provide in a real-time response to your Get Retention Message endpoint.
- [object promotionalOffer](promotionaloffer.md)
  A promotional offer and message you provide in a real-time response to your Get Retention Message endpoint.
- [object advancedCommerceInfo](advancedcommerceinfo.md)
  A response object you provide to present an offer or switch-plan recommendation message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/alternateproduct)*