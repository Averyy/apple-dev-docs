# consuming(_:startingAt:in:)

**Framework**: Foundation  
**Kind**: method

Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func consuming(_ input: String, startingAt index: String.Index, in bounds: Range<String.Index>) throws -> (upperBound: String.Index, output: Value)?
```

#### Return Value

The upper bound where the match terminates and a matched instance, or `nil` if there isn’t a match.

#### Discussion

Don’t call this method directly. Regular expression matching and capture calls it automatically when matching substrings.

## Parameters

- `input`: An input string to match against.
- `index`: The index within `input` at which to begin searching.
- `bounds`: The bounds within `input` in which to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/consuming(_:startingat:in:))*