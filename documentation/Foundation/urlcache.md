# URLCache

**Framework**: Foundation  
**Kind**: class

An object that maps URL requests to cached response objects.

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
class URLCache
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Overview

The [`URLCache`](urlcache.md) class implements the caching of responses to URL load requests, by mapping [`NSURLRequest`](nsurlrequest.md) objects to [`CachedURLResponse`](cachedurlresponse.md) objects. It provides a composite in-memory and on-disk cache, and lets you manipulate the sizes of both the in-memory and on-disk portions. You can also control the path where cache data is persistently stored.

> **Note**:  In iOS, the on-disk cache may be purged when the system runs low on disk space, but only when your app is not running.

##### Thread Safety

In iOS 8 and later, and macOS 10.10 and later, [`URLCache`](urlcache.md) is thread safe.

Although [`URLCache`](urlcache.md) instance methods can safely be called from multiple execution contexts at the same time, be aware that methods like  [`cachedResponse(for:)`](urlcache/cachedresponse(for:).md) and [`storeCachedResponse(_:for:)`](urlcache/storecachedresponse(_:for:)-7p7bl.md) have an unavoidable race condition when attempting to read or write responses for the same request.

Subclasses of [`URLCache`](urlcache.md) must implement overridden methods in such a thread-safe manner.

##### Subclassing Notes

The [`URLCache`](urlcache.md) class is meant to be used as-is, but you can subclass it when you have specific needs. For example, you might want to screen which responses are cached, or reimplement the storage mechanism for security or other reasons.

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to those that do not. Therefore, you should override the task-based methods when subclassing, as follows:

- Storing responses in the cache — Override the task-based [`storeCachedResponse(_:for:)`](urlcache/storecachedresponse(_:for:)-8uq91.md), instead of or in addition to the request-based [`storeCachedResponse(_:for:)`](urlcache/storecachedresponse(_:for:)-7p7bl.md).
- Getting responses from the cache — Override [`getCachedResponse(for:completionHandler:)`](urlcache/getcachedresponse(for:completionhandler:).md), instead of or in addition to [`cachedResponse(for:)`](urlcache/cachedresponse(for:).md).
- Removing cached responses — Override the task-based [`removeCachedResponse(for:)`](urlcache/removecachedresponse(for:)-1zwp6.md), instead of or in addition to the request-based [`removeCachedResponse(for:)`](urlcache/removecachedresponse(for:)-1dh89.md).

## Topics

### Getting and setting shared cache
- [class var shared: URLCache](urlcache/shared.md)
  The shared URL cache instance.
### Creating a new cache object
- [convenience init(memoryCapacity: Int, diskCapacity: Int, directory: URL?)](urlcache/init(memorycapacity:diskcapacity:directory:).md)
  Creates a URL cache object with the specified memory and disk capacities, in the specified directory.
- [init(memoryCapacity: Int, diskCapacity: Int, diskPath: String?)](urlcache/init(memorycapacity:diskcapacity:diskpath:).md)
  Creates a URL cache object with the specified values.
### Getting and storing cached objects
- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](urlcache/cachedresponse(for:).md)
  Returns the cached URL response in the cache for the specified URL request.
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](urlcache/storecachedresponse(_:for:)-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](urlcache/getcachedresponse(for:completionhandler:).md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](urlcache/storecachedresponse(_:for:)-8uq91.md)
  Stores a cached URL response for a specified data task.
### Removing cached objects
- [func removeCachedResponse(for: URLRequest)](urlcache/removecachedresponse(for:)-1dh89.md)
  Removes the cached URL response for a specified URL request.
- [func removeCachedResponse(for: URLSessionDataTask)](urlcache/removecachedresponse(for:)-1zwp6.md)
  Removes the cached URL response for a specified data task.
- [func removeCachedResponses(since: Date)](urlcache/removecachedresponses(since:).md)
  Clears the given cache of any cached responses since the provided date.
- [func removeAllCachedResponses()](urlcache/removeallcachedresponses.md)
  Clears the receiver’s cache, removing all stored cached URL responses.
### Getting and setting on-disk cache properties
- [var currentDiskUsage: Int](urlcache/currentdiskusage.md)
  The current size of the on-disk cache, in bytes.
- [var diskCapacity: Int](urlcache/diskcapacity.md)
  The capacity of the on-disk cache, in bytes.
### Getting and setting in-memory cache properties
- [var currentMemoryUsage: Int](urlcache/currentmemoryusage.md)
  The current size of the in-memory cache, in bytes.
- [var memoryCapacity: Int](urlcache/memorycapacity.md)
  The capacity of the in-memory cache, in bytes.
### Cache storage policies
- [URLCache.StoragePolicy](urlcache/storagepolicy.md)
  These constants specify the caching strategy used by an [`CachedURLResponse`](cachedurlresponse.md) object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Accessing cached data](accessing-cached-data.md)
  Control how URL requests make use of previously cached data.
- [class CachedURLResponse](cachedurlresponse.md)
  A cached response to a URL request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache)*