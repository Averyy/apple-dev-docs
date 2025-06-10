# canonicalRequest(for:)

**Framework**: Foundation  
**Kind**: method

Returns a canonical version of the specified request.

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
class func canonicalRequest(for request: URLRequest) -> URLRequest
```

#### Return Value

The canonical form of `request`.

#### Discussion

It is up to each concrete protocol implementation to define what “canonical” means. A protocol should guarantee that the same input request always yields the same canonical form.

Special consideration should be given when implementing this method, because the canonical form of a request is used to lookup objects in the URL cache, a process which performs equality checks between [`URLRequest`](urlrequest.md) instances.

This is an abstract method and subclasses must provide an implementation.

## Parameters

- `request`: The request whose canonical version is desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/canonicalrequest(for:))*