# minus(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes each element in another given hash table from the receiving hash table, if present.

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
func minus(_ other: NSHashTable<ObjectType>)
```

```objc
- (void) minusHashTable:(NSHashTable<id> *) other;
```

## Discussion

The equality test used for members depends on the personality option selected. For instance, choosing the [`objectPersonality`](../nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [`NSPointerFunctions.Options`](../nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## Parameters

- `other`: The hash table of elements to remove from the receiving hash table.

## See Also

### Set Functions
- [func union(NSHashTable<ObjectType>)](./union%28_%29.md)
  Adds each element in another given hash table to the receiving hash table, if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/minus(_:))*