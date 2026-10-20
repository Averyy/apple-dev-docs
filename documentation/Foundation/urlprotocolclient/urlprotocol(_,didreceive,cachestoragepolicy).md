# urlProtocol(_:didReceive:cacheStoragePolicy:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that the protocol implementation has created a response object for the request.

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
func urlProtocol(_ protocol: URLProtocol, didReceive response: URLResponse, cacheStoragePolicy policy: URLCache.StoragePolicy)
```

#### Discussion

The implementation should use the provided cache storage policy to determine whether to store the response in a cache.

## Parameters

- `protocol`: The URL protocol object sending the message.
- `response`: The newly available response object.
- `policy`: The cache storage policy for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:cachestoragepolicy:))*