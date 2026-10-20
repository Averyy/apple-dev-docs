# response

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The URL response object associated with the instance.

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
@NSCopying
var response: URLResponse { get }
```

```objc
@property (copy, readonly) NSURLResponse * response;
```

## See Also

### Getting cached URL response properties
- [var data: Data](./data.md)
  The cached response’s data.
- [var storagePolicy: URLCache.StoragePolicy](./storagepolicy.md)
  The cached response’s storage policy.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The cached response’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse/response)*