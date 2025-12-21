# input(before:)

**Framework**: Foundation  
**Kind**: method

The next input value before the given input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func input(before input: Range<Date>) -> Range<Date>?
```

#### Return Value

If [`isPositive`](date/componentsformatstyle/ispositive.md) is true, the range `input.lowerBound..<x`, where `x` is the next smaller date that this style can differentiate, or `nil` if there is no such `x` greater or equal to `input.lowerBound`. If [`isPositive`](date/componentsformatstyle/ispositive.md) is false, the range `x..<input.upperBound`, where `x` is the next smaller date this style can differentiate.

#### Discussion

If [`isPositive`](date/componentsformatstyle/ispositive.md) is true, the next input value maintains the same `lowerBound` as `input`, but has a different`upperBound`. If [`isPositive`](date/componentsformatstyle/ispositive.md) is false, the next input value maintains the same `upperBound` as `input`, but as a different `lowerBound`.

Use this function to determine if the return value provided by [`discreteInput(after:)`](date/componentsformatstyle/discreteinput(after:).md) is precise enough for your use case for any input `y`:

```None
guard let x = style.discreteInput(after: y) else {
    return
}

let z = style.input(before: x) ?? y
```

If the distance between the `upperBound`s of `z` and `x` is too large for the precision you require, you may want to manually probe `format(_:)` at a higher rate in that interval, as there is no guarantee for what the output will be in that interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle/input(before:))*