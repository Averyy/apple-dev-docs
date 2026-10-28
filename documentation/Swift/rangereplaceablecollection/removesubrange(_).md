# removeSubrange(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes the specified subrange of elements from the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeSubrange(_ bounds: Range<Self.Index>)
```

## Discussion

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeSubrange(1...3)
print(bugs)
// Prints "["Aphid", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Complexity**: O(*n*), where *n* is the length of the collection.

## Parameters

- `bounds`: The subrange of the collection to remove. The bounds of the range must be valid indices of the collection.

## Default Implementations

### RangeReplaceableCollection Implementations
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-3s5pl.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-4820q.md)
  Removes the elements in the specified subrange from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/removesubrange(_:))*