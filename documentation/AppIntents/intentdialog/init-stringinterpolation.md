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
init(stringInterpolation: String.LocalizationValue.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.

## See Also

- [init(LocalizedStringResource)](intentdialog/init(_:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(stringLiteral: String)](intentdialog/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](intentdialog/init(full:supporting:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(stringinterpolation:))*