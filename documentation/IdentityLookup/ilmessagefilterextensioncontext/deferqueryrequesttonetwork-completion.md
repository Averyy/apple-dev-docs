# deferQueryRequestToNetwork(completion:)

**Framework**: SMS and Call Reporting  
**Kind**: method

Tells the system to pass the current query request to the app extension’s associated network service.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func deferQueryRequestToNetwork() async throws -> ILNetworkResponse
```

#### Discussion

When your Message Filter app extension calls this method to defer a query to its associated server, the system performs an HTTPS network request to a URL specified in the app extension’s `Info.plist` file. The system returns the response to that request (or an error) asynchronously in an [`ILNetworkResponse`](ilnetworkresponse.md) object.

To make a network request on behalf of a Message Filter app extension, the system uses an HTTP `POST` request formatted in JSON, similar to the request shown below.

```None
POST /server-endpoint HTTP/1.1
Accept: */*
Content-Type: application/json; charset=utf-8
Content-Length: 148
```

Payload:

```json
{
    "_version": 1,
    "query": {
        "sender": "14085550001",
        "message": {
            "text": "This is a message"
        }
    },
    "app": {
        "version": "1.1"
    }
}
```

## Parameters

- `completion`: A completion block that contains either the network response to the HTTPS request or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterextensioncontext/deferqueryrequesttonetwork(completion:))*