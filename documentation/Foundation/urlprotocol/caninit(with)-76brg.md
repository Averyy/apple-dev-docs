# canInit(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Determines whether the protocol subclass can handle the specified request.

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
class func canInit(with request: URLRequest) -> Bool
```

```objc
+ (BOOL) canInitWithRequest:(NSURLRequest *) request;
```

## Return Value

[`true`](../../Swift/true.md) if the protocol subclass can handle `request`, otherwise [`false`](../../Swift/false.md).

## Discussion

A subclass should inspect `request` and determine whether or not the implementation can perform a load with that request.

This is an abstract method and subclasses must provide an implementation.

## Parameters

- `request`: The request to be handled.

## See Also

### Determining If a subclass can handle a request
- [class func canInit(with: URLSessionTask) -> Bool](./caninit%28with%29-18gbo.md)
  Determines whether the protocol subclass can handle the specified task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/caninit(with:)-76brg)*