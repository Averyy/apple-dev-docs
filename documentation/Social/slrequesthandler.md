# SLRequestHandler

**Framework**: Social  
**Kind**: typealias

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

#### Discussion

The parameters for this handler are:

Possible values are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## See Also

- [func perform(handler: SLRequestHandler!)](slrequest/perform(handler:).md)
  Performs an asynchronous request and calls the specified handler when done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequesthandler)*