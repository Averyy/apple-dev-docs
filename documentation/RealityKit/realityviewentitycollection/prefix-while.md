# prefix(while:)

**Framework**: RealityKit  
**Kind**: method

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be included or   if it should be excluded. Once the predicate   returns   it will not be called again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/prefix(while:))*