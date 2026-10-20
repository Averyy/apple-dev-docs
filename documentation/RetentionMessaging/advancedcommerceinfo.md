# advancedCommerceInfo

**Framework**: Retention Messaging API  
**Kind**: dictionary  
**Role**: Object

A response object you provide to present an offer or switch-plan recommendation message.

**Availability**:
- Retention Messaging API 1.2+

## Declaration

```
object advancedCommerceInfo
```

## Mentions

- [Retention Messaging API changelog](./retention-messaging-changelog.md)

#### Discussion

Use the `advancedCommerceInfo` object to indicate the message to display and the signed request.

Before using this object to provide a custom offer or switch-plan recommendation, ensure that the app has a default message that you’ve assigned to its generic product identifiers. For more information on setting up generic product identifiers, see Set up generic product identifiers in [Setting up your project for Advanced Commerce API](../AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce.md).

> **Note**: Providing `advancedCommerceInfo` isn’t available for subscription bundles; respond with a [`message`](./message.md) instead.

If you don’t have access to the Advanced Commerce API (ACA), use the `alternateProduct` or `promotionalOffer` keys of the [`RealtimeResponseBody`](./realtimeresponsebody.md).

For more information, see [Advanced Commerce API](../AdvancedCommerceAPI/AdvancedCommerceAPI.md).

## Properties

- `messageIdentifier` (messageIdentifier): The identifier of the message to display to the customer, along with the offer or switch-plan recommendation provided in `advancedCommerceData`.
- `advancedCommerceData` (advancedCommerceData): A Base64-encoded JSON object which contains a JWS describing an offer or switch-plan recommendation.

## See Also

### Real-time response body
- [object message](./message.md)
  A message identifier you provide in a real-time response to your Get Retention Message endpoint.
- [object alternateProduct](./alternateproduct.md)
  A switch-plan message and product ID you provide in a real-time response to your Get Retention Message endpoint.
- [object promotionalOffer](./promotionaloffer.md)
  A promotional offer and message you provide in a real-time response to your Get Retention Message endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/advancedcommerceinfo)*