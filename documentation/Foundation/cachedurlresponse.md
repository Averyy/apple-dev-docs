# CachedURLResponse

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A cached response to a URL request.

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
class CachedURLResponse
```

```objc
@interface NSCachedURLResponse : NSObject
```

## Mentions

- [Accessing cached data](./accessing-cached-data.md)

#### Overview

A [`CachedURLResponse`](./cachedurlresponse.md) object provides the server’s response metadata in the form of a [`URLResponse`](./urlresponse.md) object, along with an [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object containing the actual cached content data. Its storage policy determines whether the response should be cached on disk, in memory, or not at all.

Cached responses also contain a user info dictionary where you can store app-specific information about the cached item.

The [`URLCache`](./urlcache.md) class stores and retrieves instances of [`CachedURLResponse`](./cachedurlresponse.md).

## Topics

### Creating a cached URL response
- [init(response: URLResponse, data: Data)](./cachedurlresponse/init%28response,data%29.md)
  Creates a cached URL response instance.
- [init(response: URLResponse, data: Data, userInfo: [AnyHashable : Any]?, storagePolicy: URLCache.StoragePolicy)](./cachedurlresponse/init%28response,data,userinfo,storagepolicy%29.md)
  Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.
### Getting cached URL response properties
- [var data: Data](./cachedurlresponse/data.md)
  The cached response’s data.
- [var response: URLResponse](./cachedurlresponse/response.md)
  The URL response object associated with the instance.
- [var storagePolicy: URLCache.StoragePolicy](./cachedurlresponse/storagepolicy.md)
  The cached response’s storage policy.
- [var userInfo: [AnyHashable : Any]?](./cachedurlresponse/userinfo.md)
  The cached response’s user info dictionary.
### Setting cache storage policies
- [URLCache.StoragePolicy](./urlcache/storagepolicy.md)
  These constants specify the caching strategy used by an [`CachedURLResponse`](./cachedurlresponse.md) object.
### Initializers
- [init?(coder: NSCoder)](./cachedurlresponse/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Cache behavior
- [Accessing cached data](./accessing-cached-data.md)
  Control how URL requests make use of previously cached data.
- [class URLCache](./urlcache.md)
  An object that maps URL requests to cached response objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cachedurlresponse)*