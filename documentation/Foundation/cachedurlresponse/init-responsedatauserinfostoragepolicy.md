# init(response:data:userInfo:storagePolicy:)

**Framework**: Foundation  
**Kind**: init

Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.

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
init(response: URLResponse, data: Data, userInfo: [AnyHashable : Any]? = nil, storagePolicy: URLCache.StoragePolicy)
```

#### Return Value

A cached URL response object, containing the response and data.

## Parameters

- `response`: The response to cache.
- `data`: The data to cache.
- `userInfo`: An optional dictionary of user information. May be  .
- `storagePolicy`: The storage policy for the cached response.

## See Also

- [init(response: URLResponse, data: Data)](cachedurlresponse/init(response:data:).md)
  Creates a cached URL response instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse/init(response:data:userinfo:storagepolicy:))*