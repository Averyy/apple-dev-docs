# initWithMemoryCapacity:diskCapacity:directoryURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (instancetype) initWithMemoryCapacity:(NSUInteger) memoryCapacity diskCapacity:(NSUInteger) diskCapacity directoryURL:(NSURL *) directoryURL;
```

#### Discussion

A disk cache measured in the tens of megabytes should be acceptable in most cases.

## Parameters

- `memoryCapacity`: The memory capacity of the cache, in bytes.
- `diskCapacity`: The disk capacity of the cache, in bytes.
- `directoryURL`: The path to an on-disk directory at which to store the on-disk cache. If `directory` is `nil`, the cache uses a default directory.

## See Also

### Creating a new cache object
- [init(memoryCapacity: Int, diskCapacity: Int, diskPath: String?)](../urlcache/init%28memorycapacity,diskcapacity,diskpath%29.md)
  Creates a URL cache object with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcache/initwithmemorycapacity:diskcapacity:directoryurl:)*