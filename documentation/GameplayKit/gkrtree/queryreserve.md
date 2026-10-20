# queryReserve

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The number of elements to reserve space for when searching.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var queryReserve: Int { get set }
```

```objc
@property NSUInteger queryReserve;
```

#### Discussion

Use this property to optimize for search speed at the cost of memory usage during a search. With the default value of `1`, when you use the [`elements(inBoundingRectMin:rectMax:)`](./elements%28inboundingrectmin,rectmax%29.md) method, the tree examines potential search results one at a time. If you specify a larger number, the tree allocates additional memory to process several elements together when searching.

## See Also

### Searching for Elements
- [func elements(inBoundingRectMin: vector_float2, rectMax: vector_float2) -> [ElementType]](./elements%28inboundingrectmin,rectmax%29.md)
  Searches the tree and returns all elements found within the specified bounding region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrtree/queryreserve)*