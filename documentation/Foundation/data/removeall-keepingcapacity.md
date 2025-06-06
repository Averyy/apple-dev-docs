# removeAll(keepingCapacity:)

**Framework**: Foundation  
**Kind**: method

Removes all elements from the collection.

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
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

#### Discussion

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

## Parameters

- `keepCapacity`: Pass   to request that the collection   avoid releasing its storage. Retaining the collection’s storage can   be a useful optimization when you’re planning to grow the collection   again. The default value is  .

## See Also

- [func remove(at: Self.Index) -> Self.Element](data/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeSubrange(Range<Self.Index>)](data/removesubrange(_:)-8ohtp.md)
  Removes the elements in the specified subrange from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removeall(keepingcapacity:))*