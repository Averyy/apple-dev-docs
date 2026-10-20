# canHandle(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns whether a request can be handled based on a preflight evaluation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func canHandle(_ request: URLRequest) -> Bool
```

```objc
+ (BOOL) canHandleRequest:(NSURLRequest *) request;
```

#### Return Value

[`true`](../../Swift/true.md) if a preflight operation determines that a connection with `request` can be created and the associated I/O can be started, [`false`](../../Swift/false.md) otherwise.

#### Discussion

The result of this method is valid as long as no [`URLProtocol`](../urlprotocol.md) classes are registered or unregistered, and `request` remains unchanged. Applications should be prepared to handle failures even if they have performed request preflighting by calling this method.

## Parameters

- `request`: The request to evaluate. The connection deep-copies the request on creation.

## See Also

### Related Documentation
- [class func unregisterClass(AnyClass)](../urlprotocol/unregisterclass%28_%29.md)
  Unregisters the specified subclass of [`URLProtocol`](../urlprotocol.md).
- [class func registerClass(AnyClass) -> Bool](../urlprotocol/registerclass%28_%29.md)
  Attempts to register a subclass of [`URLProtocol`](../urlprotocol.md), making it visible to the URL loading system.
- [URL Loading System](../url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/canhandle(_:))*