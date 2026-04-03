# RealtimeResponseBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

A response you provide to choose, in real time, a retention message the system displays to the customer.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object RealtimeResponseBody
```

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)

#### Discussion

Return this response when the App Store calls your `Get Retention Message` endpoint.

In this response, you select a retention message in real time for the system to display to your customer. Choose a message based on your business needs and by considering the information you receive in [`RealtimeRequestBody`](realtimerequestbody.md).

All messages and images need to be in an `APPROVED` state for the system to display them to customers. For more information, see [`Setting up retention messages`](setting-up-retention-messages.md), and  [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

For more information on the Advanced Commerce API, see [`Advanced Commerce API`](https://developer.apple.com/documentation/AdvancedCommerceAPI).

## Properties

- `message` (message): A retention message that’s text-based and can include an optional image. If you supply this field, don’t include the other fields.
- `alternateProduct` (alternateProduct): A retention message with a switch-plan option. If you supply this field, don’t include the other fields.
- `promotionalOffer` (promotionalOffer): A retention message that includes a promotional offer. If you supply this field, don’t include the other fields.
- `advancedCommerceInfo` (advancedCommerceInfo): A retention offer or switch plan option. If you pass this object for a subscription that’s not an Advanced Commerce subscription, the framework treats the request as invalid and ignores the response. If you supply this field, don’t include the other fields.

## See Also

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/realtimeresponsebody)*