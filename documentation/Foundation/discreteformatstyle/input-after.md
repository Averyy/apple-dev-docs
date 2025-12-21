# input(after:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

The next input value after the given input.

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
func input(after input: Self.FormatInput) -> Self.FormatInput?
```

#### Return Value

The next “greater” input value that can be represented by [`FormatInput`](formatstyle/formatinput.md) or an underlying representation the format style uses internally.

#### Discussion

Use this function to determine if the return value provided by [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) is precise enough for your use case for any input `y`:

```swift
guard let x = style.discreteInput(before: y) else {
    return
}

let z = style.input(after: x) ?? y
```

If the distance between `x` and `z` is too large for the precision you require, you may want to manually probe [`format(_:)`](formatstyle/format(_:).md) at a higher rate in that interval, as there is no guarantee for what the output will be in that interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discreteformatstyle/input(after:))*