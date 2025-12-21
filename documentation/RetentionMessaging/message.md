# message

**Framework**: Retention Messaging API  
**Kind**: dictionary

A message identifier you provide in a real-time response to your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object message
```

#### Discussion

In your [`RealtimeResponseBody`](realtimeresponsebody.md) real-time response, you can choose from mutually exclusive options. Include `message` in your response to provide a text-based message (with or without an image) as the retention message the system displays to the customer.

The message identifier needs to refer to a message that has a [`messageState`](messagestate.md) of `APPROVED`; otherwise, the retention message fails. If the message includes an image, the image also needs to have an [`imageState`](imagestate.md) of `APPROVED`. For more information about setting up messages, see [`Setting up retention messages`](setting-up-retention-messages.md).

## See Also

- [object alternateProduct](alternateproduct.md)
  A switch-plan message and product ID you provide in a real-time response to your Get Retention Message endpoint.
- [object promotionalOffer](promotionaloffer.md)
  A promotional offer and message you provide in a real-time response to your Get Retention Message endpoint.
- [object advancedCommerceInfo](advancedcommerceinfo.md)
  A response object you provide to present an offer or switch-plan recommendation message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/message)*