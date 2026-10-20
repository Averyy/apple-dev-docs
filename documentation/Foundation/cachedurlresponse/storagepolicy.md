# storagePolicy

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cached response’s storage policy.

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
var storagePolicy: URLCache.StoragePolicy { get }
```

```objc
@property (readonly) NSURLCacheStoragePolicy storagePolicy;
```

## Mentions

- [Accessing cached data](../accessing-cached-data.md)

## See Also

### Getting cached URL response properties
- [var data: Data](./data.md)
  The cached response’s data.
- [var response: URLResponse](./response.md)
  The URL response object associated with the instance.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The cached response’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse/storagepolicy)*