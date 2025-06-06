# removeAll(where:)

**Framework**: System  
**Kind**: method

Removes all the elements that satisfy the given predicate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

#### Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the vowels from a string:

```swift
var phrase = "The rain in Spain stays mainly in the plain."

let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
phrase.removeAll(where: { vowels.contains($0) })
// phrase == "Th rn n Spn stys mnly n th pln."
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `shouldBeRemoved`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be removed from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/removeall(where:))*