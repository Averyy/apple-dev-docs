# init(stringInterpolation:)

**Framework**: App Intents  
**Kind**: init

Creates an instance from a string interpolation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(stringInterpolation: ParameterSummaryString<Intent>.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.

## See Also

- [init(String)](parametersummarystring/init(_:).md)
- [init(stringLiteral: String)](parametersummarystring/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [ParameterSummaryString.StringInterpolation](parametersummarystring/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarystring/init(stringinterpolation:))*