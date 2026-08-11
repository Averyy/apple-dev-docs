# nextSpan(maxCount:)

**Framework**: Swift  
**Kind**: method

Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func nextSpan(maxCount: Int) -> Span<Iterator.Element>
```

#### Discussion

If the underlying type stores its elements in one or more blocks of contiguous memory, then the returned span typically directly addresses one of those buffers. On the other hand, if the underlying type materializes its elements on demand, then the returned span addresses a temporary buffer managed by the iterator itself. Consequently, the returned span is tied to this particular invocation of `nextSpan`, and it cannot survive beyond the next invocation of this method.

If the iterator has not yet reached the end of the underlying elements, then this method returns a non-empty span of at most `maxCount` elements and updates the iterator’s current position to the element following the last item in the returned span. The `maxCount` argument allows callers to avoid getting more items than they are able to process in one go, simplifying usage, and avoiding materializing more elements than needed.

If the iterator’s current position is at the end of the container, then this method returns an empty span without updating the position.

This method can be used to efficiently process the items of a container in bulk, by directly iterating over its piecewise contiguous pieces of storage:

```swift
var it = items.makeBorrowingIterator()
while true {
  let span = it.nextSpan(maxCount: .max)
  if span.isEmpty { break }
  // Process items in `span`
}
```

The spans returned by this method are not guaranteed to be disjunct. Iterators that materialize elements on demand typically reuse the same buffer over and over again; and even some proper containers may link to a single storage chunk (or parts of a storage chunk) multiple times, for example to repeat their contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratoradapter/nextspan(maxcount:))*