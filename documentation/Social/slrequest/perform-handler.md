# perform(handler:)

**Framework**: Social  
**Kind**: method

Performs an asynchronous request and calls the specified handler when done.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func perform(handler: SLRequestHandler!)
```

## Parameters

- `handler`: The handler to call when the request is done. The parameters for this handler are described in  . This handler is not guaranteed to be called on any particular thread and should not be nil.

## See Also

- [typealias SLRequestHandler](slrequesthandler.md)
  The callback handler for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/perform(handler:))*