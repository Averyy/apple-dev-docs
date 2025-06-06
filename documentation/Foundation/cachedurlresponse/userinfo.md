# userInfo

**Framework**: Foundation  
**Kind**: property

The cached response’s user info dictionary.

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
var userInfo: [AnyHashable : Any]? { get }
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

This value is `nil` if there is no user info dictionary.

## See Also

- [var data: Data](cachedurlresponse/data.md)
  The cached response’s data.
- [var response: URLResponse](cachedurlresponse/response.md)
  The URL response object associated with the instance.
- [var storagePolicy: URLCache.StoragePolicy](cachedurlresponse/storagepolicy.md)
  The cached response’s storage policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse/userinfo)*