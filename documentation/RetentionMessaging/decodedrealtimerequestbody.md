# DecodedRealtimeRequestBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

The decoded request body the App Store sends to your server to request a real-time retention message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object DecodedRealtimeRequestBody
```

## Mentions

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
- [Retention Messaging API changelog](retention-messaging-changelog.md)
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)

#### Discussion

The App Store server sends a request to your `Get Retention Message` endpoint that includes a [`RealtimeRequestBody`](realtimerequestbody.md). The `DecodedRealtimeRequestBody` is the decoded version of that request body.

The `DecodedRealtimeRequestBody` provides information you can use to select a retention message for display. The request includes the customer’s original transaction identifier, the product identifier, and their locale. Consider this information, along with your business logic, to choose the best retention message for the customer.

> ❗ **Important**: Always check that the `appAppleId` in the request matches your app’s `appAppleId`. If it doesn’t match, don’t respond to the request.

For more information, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object RealtimeRequestBody](realtimerequestbody.md)
  The request body the App Store server sends to your Get Retention Message endpoint.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/decodedrealtimerequestbody)*