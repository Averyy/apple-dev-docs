# handle(_:context:completion:)

**Framework**: SMS and Call Reporting  
**Kind**: method  
**Required**: Yes

Evaluates a query request and tells the system how to handle the message represented in the request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func handle(_ queryRequest: ILMessageFilterQueryRequest, context: ILMessageFilterExtensionContext) async -> ILMessageFilterQueryResponse
```

## Parameters

- `queryRequest`: A query request that describes a received message.
- `context`: The app extension context that defines APIs to defer the request to a server, if necessary.
- `completion`: A completion block used to return a response that describes how to handle the message. You can invoke this block asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryhandling/handle(_:context:completion:))*