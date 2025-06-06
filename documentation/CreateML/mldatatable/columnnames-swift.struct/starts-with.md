# starts(with:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix) -> Bool where PossiblePrefix : Sequence, Self.Element == PossiblePrefix.Element
```

#### Return Value

`true` if the initial elements of the sequence are the same as the elements of `possiblePrefix`; otherwise, `false`. If `possiblePrefix` has no elements, the return value is `true`.

#### Discussion

This example tests whether one countable range begins with the elements of another countable range.

```None
let a = 1...3
let b = 1...10

print(b.starts(with: a))
// Prints "true"
```

Passing a sequence with no elements or an empty collection as `possiblePrefix` always results in `true`.

```None
print(b.starts(with: []))
// Prints "true"
```

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `possiblePrefix`.

O(), where  is the lesser of the length of the sequence and the length of `possiblePrefix`.

## Parameters

- `possiblePrefix`: A sequence to compare to this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct/starts(with:))*