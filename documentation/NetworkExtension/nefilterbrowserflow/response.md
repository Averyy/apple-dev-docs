# response

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSURLResponse * response;
```

#### Discussion

This property will be nil until some incoming data is received for this flow.

## See Also

### Getting browser flow properties
- [var parentURL: URL?](./parenturl.md)
  A URL of the web page that’s responsible for the flow’s creation.
- [var request: URLRequest?](./request.md)
  An HTTP request of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/response)*