# elementsEqual(_:)

**Framework**: System  
**Kind**: method

Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.

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
func elementsEqual<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

#### Return Value

`true` if this sequence and `other` contain the same elements in the same order.

#### Discussion

At least one of the sequences must be finite.

This example tests whether one countable range shares the same elements as another countable range and an array.

```swift
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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/elementsequal(_:))*