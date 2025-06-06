# diskCapacity

**Framework**: Foundation  
**Kind**: property

The capacity of the on-disk cache, in bytes.

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
var diskCapacity: Int { get set }
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

When set, the on-disk cache will truncate its contents to the given size, if necessary.

## See Also

- [var currentDiskUsage: Int](urlcache/currentdiskusage.md)
  The current size of the on-disk cache, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/diskcapacity)*