# shared

**Framework**: Foundation  
**Kind**: property

The shared URL cache instance.

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
class var shared: URLCache { get set }
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

If your app doesn’t have special caching requirements or constraints, the default shared cache instance should be acceptable. Alternatively, you can create a custom [`URLCache`](urlcache.md) object and set it as the shared cache instance (use `+[NSURLCache setSharedURLCache]` in Objective-C). You should do so before making any calls to this method.

## See Also

- [Accessing cached data](accessing-cached-data.md)
  Control how URL requests make use of previously cached data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/shared)*