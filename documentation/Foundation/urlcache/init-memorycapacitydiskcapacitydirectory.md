# init(memoryCapacity:diskCapacity:directory:)

**Framework**: Foundation  
**Kind**: init

Creates a URL cache object with the specified memory and disk capacities, in the specified directory.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(memoryCapacity: Int, diskCapacity: Int, directory: URL? = nil)
```

#### Discussion

A disk cache measured in the tens of megabytes is acceptable in most cases.

## Parameters

- `memoryCapacity`: The memory capacity of the cache, in bytes.
- `diskCapacity`: The disk capacity of the cache, in bytes.
- `directory`: The path to an on-disk directory, where the system stores the on-disk cache. If   is  , the cache uses a default directory.

## See Also

- [init(memoryCapacity: Int, diskCapacity: Int, diskPath: String?)](urlcache/init(memorycapacity:diskcapacity:diskpath:).md)
  Creates a URL cache object with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:directory:))*