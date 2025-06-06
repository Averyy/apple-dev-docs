# makeCache(subviews:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates and initializes a cache for a layout instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func makeCache(subviews: Self.Subviews) -> Self.Cache
```

#### Return Value

Storage for calculated data that you share among the methods of your custom layout container.

#### Discussion

You can optionally use a cache to preserve calculated values across calls to a layout container’s methods. Many layout types don’t need a cache, because SwiftUI automatically reuses both the results of calls into the layout and the values that the layout reads from its subviews. Rely on the protocol’s default implementation of this method if you don’t need a cache.

However you might find a cache useful when:

- The layout container repeats complex, intermediate calculations across calls like [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md), [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md), and [`explicitAlignment(of:in:proposal:subviews:cache:)`](layout/explicitalignment(of:in:proposal:subviews:cache:).md). You might be able to improve performance by calculating values once and storing them in a cache.
- The layout container reads many [`LayoutValueKey`](layoutvaluekey.md) values from subviews. It might be more efficient to do that once and store the results in the cache, rather than rereading the subviews’ values before each layout call.
- You want to maintain working storage, like temporary Swift arrays, across calls into the layout, to minimize the number of allocation events.

Only implement a cache if profiling shows that it improves performance.

##### Initialize a Cache

Implement the `makeCache(subviews:)` method to create a cache. You can add computed values to the cache right away, using information from the `subviews` input parameter, or you can do that later. The methods of the [`Layout`](layout.md) protocol that can access the cache take the cache as an in-out parameter, which enables you to modify the cache anywhere that you can read it.

You can use any storage type that makes sense for your layout algorithm, but be sure that you only store data that you derive from the layout and its subviews (lazily, if possible). For this to work correctly, SwiftUI needs to be able to call this method to recreate the cache without changing the layout result.

When you return a cache from this method, you implicitly define a type for your cache. Be sure to either make the type of the `cache` parameters on your other [`Layout`](layout.md) protocol methods match, or use a type alias to define the [`Cache`](layout/cache.md) associated type.

##### Update the Cache

If the layout container or any of its subviews change, SwiftUI calls the [`updateCache(_:subviews:)`](layout/updatecache(_:subviews:).md) method so you can modify or invalidate the contents of the cache. The default implementation of that method calls the `makeCache(subviews:)` method to recreate the cache, but you can provide your own implementation of the update method to take an incremental approach, if appropriate.

## Parameters

- `subviews`: A collection of proxy instances that represent the   views that the container arranges. You can use the proxies in the   collection to get information about the subviews as you   calculate values to store in the cache.

## See Also

- [func updateCache(inout Self.Cache, subviews: Self.Subviews)](layout/updatecache(_:subviews:).md)
  Updates the layout’s cache when something changes.
- [associatedtype Cache = Void](layout/cache.md)
  Cached values associated with the layout instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/makecache(subviews:))*