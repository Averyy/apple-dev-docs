# remove(_:)

**Framework**: Foundation  
**Kind**: method

Removes a given object from the set.

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
func remove(_ object: Any)
```

#### Discussion

If `object` is present in the set, decrements the count associated with it. If the count is decremented to `0`, `object` is removed from the set. [`remove(_:)`](nscountedset/remove(_:).md) does nothing if `object` is not present in the set.

## Parameters

- `object`: The object to remove from the set.

## See Also

- [func count(for: Any) -> Int](nscountedset/count(for:).md)
  Returns the count associated with a given object in the set.
- [func add(Any)](nscountedset/add(_:).md)
  Adds a given object to the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/remove(_:))*