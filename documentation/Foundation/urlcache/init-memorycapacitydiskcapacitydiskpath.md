# init(memoryCapacity:diskCapacity:diskPath:)

**Framework**: Foundation  
**Kind**: init

Creates a URL cache object with the specified values.

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
init(memoryCapacity: Int, diskCapacity: Int, diskPath path: String?)
```

#### Return Value

The initialized cache object.

#### Discussion

The returned cache instance is backed by disk, so you have more leeway when choosing the capacity for this kind of cache. A disk cache measured in the tens of megabytes should be acceptable in most cases.

## Parameters

- `memoryCapacity`: The memory capacity of the cache, in bytes.
- `diskCapacity`: The disk capacity of the cache, in bytes.
- `path`: In iOS,   is the name of a subdirectory of the application’s default cache directory in which to store the on-disk cache (the subdirectory is created if it does not exist).

## See Also

- [class var shared: URLCache](urlcache/shared.md)
  The shared URL cache instance.
- [convenience init(memoryCapacity: Int, diskCapacity: Int, directory: URL?)](urlcache/init(memorycapacity:diskcapacity:directory:).md)
  Creates a URL cache object with the specified memory and disk capacities, in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:diskpath:))*