# SLRequestHandler

**Framework**: Social  
**Kind**: typealias  
**Role**: Type Alias

The callback handler for a request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
typealias SLRequestHandler = (Data?, HTTPURLResponse?, (any Error)?) -> Void
```

```c
typedef void (^)(NSData *, NSHTTPURLResponse *, NSError *) SLRequestHandler;
```

#### Discussion

The parameters for this handler are:

- **`responseData`**: The data returned by the request. The format of this data is dependent on the target service.
- **`urlResponse`**: The URL response returned by the request that includes the HTTP response codes.
- **`error`**: An error identifier.

Possible values are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](./slrequest.md).

## See Also

### Sending a Request
- [func perform(handler: SLRequestHandler!)](./slrequest/perform%28handler%29.md)
  Performs an asynchronous request and calls the specified handler when done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequesthandler)*