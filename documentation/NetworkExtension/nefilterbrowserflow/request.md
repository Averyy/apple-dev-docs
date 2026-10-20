# request

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An HTTP request of the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var request: URLRequest? { get }
```

```objc
@property (readonly, nullable) NSURLRequest * request;
```

## See Also

### Getting browser flow properties
- [var parentURL: URL?](./parenturl.md)
  A URL of the web page that’s responsible for the flow’s creation.
- [var response: URLResponse?](./response.md)
  An HTTP response of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/request)*