# handle(_:context:completion:)

**Framework**: SMS and Call Reporting  
**Kind**: method  
**Required**: Yes

Evaluates a query request and provides a response describing how the system should handle the message it represents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func handle(_ capabilitiesQueryRequest: ILMessageFilterCapabilitiesQueryRequest, context: ILMessageFilterExtensionContext) async -> ILMessageFilterCapabilitiesQueryResponse
```

## Parameters

- `capabilitiesQueryRequest`: A query request that describes a received message.
- `context`: The app extension context that defines APIs to defer the request to a server, if necessary.
- `completion`: A completion block used to return a response that describes how to handle the message. You can invoke this block asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltercapabilitiesqueryhandling/handle(_:context:completion:))*