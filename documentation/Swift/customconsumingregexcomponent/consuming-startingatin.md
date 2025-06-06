# consuming(_:startingAt:in:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

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
func consuming(_ input: String, startingAt index: String.Index, in bounds: Range<String.Index>) throws -> (upperBound: String.Index, output: Self.RegexOutput)?
```

#### Return Value

The upper bound where the match terminates and a matched instance, or `nil` if there isn’t a match.

## Parameters

- `input`: The string in which the match is performed.
- `index`: An index of   at which to begin matching.
- `bounds`: The bounds in   in which the match is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/customconsumingregexcomponent/consuming(_:startingat:in:))*