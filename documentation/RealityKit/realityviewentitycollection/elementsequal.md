# elementsEqual(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

#### Return Value

`true` if this sequence and `other` contain the same elements in the same order.

#### Discussion

At least one of the sequences must be finite.

This example tests whether one countable range shares the same elements as another countable range and an array.

```None
let a = 1...3
let b = 1...10

print(a.elementsEqual(b))
// Prints "false"
print(a.elementsEqual([1, 2, 3]))
// Prints "true"
```

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `other`.

O(), where  is the lesser of the length of the sequence and the length of `other`.

## Parameters

- `other`: A sequence to compare to this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/elementsequal(_:))*