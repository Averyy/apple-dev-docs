# promotionalOffer

**Framework**: Retention Messaging API  
**Kind**: dictionary

A promotional offer and message you provide in a real-time response to your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object promotionalOffer
```

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

In your [`RealtimeResponseBody`](realtimeresponsebody.md) real-time response, you can choose from mutually exclusive options. Include `promotionalOffer` in your response to provide a retention message with a promotional offer. The message identifier needs to refer to a message that doesn’t have an image, and that has a [`messageState`](messagestate.md) of `APPROVED`; otherwise, the retention message fails. For more information about setting up messages, see [`Upload Message`](upload-message.md).

For new implementations, consider using the [`promotionalOfferSignatureV2`](promotionaloffersignaturev2.md) signature, which is easier to generate.

For more information on generating the signatures, see [`promotionalOfferSignatureV1`](promotionaloffersignaturev1.md) and [`promotionalOfferSignatureV2`](promotionaloffersignaturev2.md).

## See Also

- [object message](message.md)
  A message identifier you provide in a real-time response to your Get Retention Message endpoint.
- [object alternateProduct](alternateproduct.md)
  A switch-plan message and product ID you provide in a real-time response to your Get Retention Message endpoint.
- [object advancedCommerceInfo](advancedcommerceinfo.md)
  A response object you provide to present an offer or switch-plan recommendation message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/promotionaloffer)*