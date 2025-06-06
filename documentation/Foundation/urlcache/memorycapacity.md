# memoryCapacity

**Framework**: Foundation  
**Kind**: property

The capacity of the in-memory cache, in bytes.

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
var memoryCapacity: Int { get set }
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

At the time this property is set, the in-memory cache will truncate its contents to the size given, if necessary.

## See Also

- [var currentMemoryUsage: Int](urlcache/currentmemoryusage.md)
  The current size of the in-memory cache, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/memorycapacity)*