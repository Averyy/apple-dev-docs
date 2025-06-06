# response

**Framework**: Network Extension  
**Kind**: property

An HTTP response of the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var response: URLResponse? { get }
```

#### Discussion

This property will be nil until some incoming data is received for this flow.

## See Also

- [var parentURL: URL?](nefilterbrowserflow/parenturl.md)
  A URL of the web page that’s responsible for the flow’s creation.
- [var request: URLRequest?](nefilterbrowserflow/request.md)
  An HTTP request of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/response)*