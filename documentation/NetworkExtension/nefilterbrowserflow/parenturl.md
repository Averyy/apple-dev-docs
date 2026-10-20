# parentURL

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A URL of the web page that’s responsible for the flow’s creation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var parentURL: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * parentURL;
```

#### Discussion

This property will be non-nil only if the flow is loading a resource into a frame. In that case, this property will be set to the URL of the web page containing the frame.

## See Also

### Getting browser flow properties
- [var request: URLRequest?](./request.md)
  An HTTP request of the flow.
- [var response: URLResponse?](./response.md)
  An HTTP response of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/parenturl)*