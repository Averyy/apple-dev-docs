# removeSubranges(_:)

**Framework**: Swift  
**Kind**: method

Removes the elements at the given indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func removeSubranges(_ subranges: RangeSet<Self.Index>)
```

#### Discussion

For example, this code sample finds the indices of all the vowel characters in the string, and then removes those characters.

```swift
var str = "The rain in Spain stays mainly in the plain."
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let vowelIndices = str.indices(where: { vowels.contains($0) })

str.removeSubranges(vowelIndices)
// str == "Th rn n Spn stys mnly n th pln."
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `subranges`: The indices of the elements to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/removesubranges(_:)-2ncra)*