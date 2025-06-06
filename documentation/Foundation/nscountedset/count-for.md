# count(for:)

**Framework**: Foundation  
**Kind**: method

Returns the count associated with a given object in the set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func count(for object: Any) -> Int
```

#### Return Value

The count associated with `object` in the set, which can be thought of as the number of occurrences of `object` present in the set.

## Parameters

- `object`: The object for which to return the count.

## See Also

- [var count: Int](nsset/count.md)
  The number of members in the set.
- [func objectEnumerator() -> NSEnumerator](nscountedset/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the set once, independent of its count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/count(for:))*