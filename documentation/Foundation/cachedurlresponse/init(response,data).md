# init(response:data:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a cached URL response instance.

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
init(response: URLResponse, data: Data)
```

```objc
- (instancetype) initWithResponse:(NSURLResponse *) response data:(NSData *) data;
```

#### Return Value

A cached URL response object, containing the response and data.

#### Discussion

The cache storage policy is set to the default, [`URLCache.StoragePolicy.allowed`](../urlcache/storagepolicy/allowed.md), and the user info dictionary is set to `nil`.

## Parameters

- `response`: The response to cache.
- `data`: The data to cache.

## See Also

### Creating a cached URL response
- [init(response: URLResponse, data: Data, userInfo: [AnyHashable : Any]?, storagePolicy: URLCache.StoragePolicy)](./init%28response,data,userinfo,storagepolicy%29.md)
  Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse/init(response:data:))*