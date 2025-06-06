# prefix(while:)

**Framework**: Createmlcomponents  
**Kind**: method

Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> [Self.Element]
```

#### Return Value

A sequence of the initial, consecutive elements that satisfy `predicate`.

#### Discussion

The following example uses the `prefix(while:)` method to find the positive numbers at the beginning of the `numbers` array. Every element of `numbers` up to, but not including, the first negative value is included in the result.

```None
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
let positivePrefix = numbers.prefix(while: { $0 > 0 })
// positivePrefix == [3, 7, 4]
```

If `predicate` matches every element in the sequence, the resulting sequence contains every element of the sequence.

> **Note**: O(), where  is the length of the result.

## Parameters

- `predicate`: A closure that takes an element of the sequence as   its argument and returns a Boolean value indicating whether the   element should be included in the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows/prefix(while:))*