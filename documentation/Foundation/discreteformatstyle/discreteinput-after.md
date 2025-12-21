# discreteInput(after:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

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
func discreteInput(after input: Self.FormatInput) -> Self.FormatInput?
```

#### Return Value

For most `input`s, the method returns the “smallest” value “greater” than `input` for which the style produces a different [`FormatOutput`](formatstyle/formatoutput.md), or `nil` if no such value exists. For some input values, the function may also return a value “greater” than `input` for which the style still produces the same [`FormatOutput`](formatstyle/formatoutput.md) as for `input`.

#### Discussion

Use this function to determine the next “greater” input that warrants updating the formatted output. The following example prints all possible outputs the format style can produce upwards starting from the `startInput`:

```swift
var previousInput = startInput
while let nextInput = style.discreteInput(after: previousInput) {
    print(style.format(nextInput))
    previousInput = nextInput
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discreteformatstyle/discreteinput(after:))*