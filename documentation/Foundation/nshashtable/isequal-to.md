# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given hash table is equal to the receiving hash table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to other: NSHashTable<ObjectType>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the contents of `other` are equal to the contents of the receiving hash table, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Two hash tables have equal contents if they each have the same number of members and if each member of one hash table is present in the other.

The equality test used for members depends on the personality option selected. For instance, choosing the [`objectPersonality`](nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [`NSPointerFunctions.Options`](nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## Parameters

- `other`: The hash table with which to compare the receiving hash table.

## See Also

- [func intersect(NSHashTable<ObjectType>)](nshashtable/intersect(_:).md)
  Removes from the receiving hash table each element that isn’t a member of another given hash table.
- [func intersects(NSHashTable<ObjectType>) -> Bool](nshashtable/intersects(_:).md)
  Returns a Boolean value that indicates whether a given hash table intersects with the receiving hash table.
- [func isSubset(of: NSHashTable<ObjectType>) -> Bool](nshashtable/issubset(of:).md)
  Returns a Boolean value that indicates whether every element in the receiving hash table is also present in another given hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/isequal(to:))*