# removeSubrange(_:)

**Framework**: Swift  
**Kind**: method  
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

#### Discussion

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeSubrange(1...3)
print(bugs)
// Prints "["Aphid", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `bounds`: The subrange of the collection to remove. The bounds   of the range must be valid indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/removesubrange(_:))*