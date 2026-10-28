# init(memoryCapacity:diskCapacity:diskPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL cache object with the specified values.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
init(memoryCapacity: Int, diskCapacity: Int, diskPath path: String?)
```

```objc
- (instancetype) initWithMemoryCapacity:(NSUInteger) memoryCapacity diskCapacity:(NSUInteger) diskCapacity diskPath:(NSString *) path;
```

## Return Value

The initialized cache object.

## Discussion

The returned cache instance is backed by disk, so you have more leeway when choosing the capacity for this kind of cache. A disk cache measured in the tens of megabytes should be acceptable in most cases.

## Parameters

- `memoryCapacity`: The memory capacity of the cache, in bytes.
- `diskCapacity`: The disk capacity of the cache, in bytes.
- `path`: In macOS, `path` is the location at which to store the on-disk cache.

  In iOS, `path` is the name of a subdirectory of the application’s default cache directory in which to store the on-disk cache (the subdirectory is created if it does not exist).

## See Also

### Related Documentation
- [class var shared: URLCache](./shared.md)
  The shared URL cache instance.
### Creating a new cache object
- [convenience init(memoryCapacity: Int, diskCapacity: Int, directory: URL?)](./init%28memorycapacity,diskcapacity,directory%29.md)
  Creates a URL cache object with the specified memory and disk capacities, in the specified directory.
- [- initWithMemoryCapacity:diskCapacity:directoryURL:](../nsurlcache/initwithmemorycapacity_diskcapacity_directoryurl_.md)
  Creates a URL cache object with the specified memory and disk capacities, in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:diskpath:))*