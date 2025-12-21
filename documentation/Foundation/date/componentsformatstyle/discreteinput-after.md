# discreteInput(after:)

**Framework**: Foundation  
**Kind**: method

The next discretization boundary after the given input.

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
func discreteInput(after input: Range<Date>) -> Range<Date>?
```

#### Return Value

If [`isPositive`](date/componentsformatstyle/ispositive.md) is true, the range `input.lowerBound..<x`, where `x` is the greatest date that is smaller than `input.upperBound` for which this style might produce a different [`FormatOutput`](formatstyle/formatoutput.md). If [`isPositive`](date/componentsformatstyle/ispositive.md) is false, the range `x..<input.upperBound`, where `x` is the smallest date that is greater than `input.lowerBound` for which this style might produce a different [`FormatOutput`](formatstyle/formatoutput.md). The function may return `nil` if there is no such value smaller or equal to `input.upperBound`.

#### Discussion

Use this function to determine the next greater input that warrants updating the formatted output. If [`isPositive`](date/componentsformatstyle/ispositive.md) is true, the returned range has the same `lowerBound` as the `input`, but increases the `upperBound` so that the returned range produces the next greater output. If [`isPositive`](date/componentsformatstyle/ispositive.md) is false, the returned range has the same `upperBound` as the `input` and a greater `lowerBound`.

```None
let style = Date.ComponentsFormatStyle(style: .wide)
print(style.format(start..<end)) // "1 hour"
guard let next = style.discreteInput(after: start..<end) else {
    return
}
print(style.format(next)) // "1 hour, 1 second"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle/discreteinput(after:))*