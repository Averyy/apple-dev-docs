# init(full:supporting:)

**Framework**: App Intents  
**Kind**: init

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

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
init(full: LocalizedStringResource, supporting: LocalizedStringResource)
```

#### Discussion

Parameters:

- full: a standalone message that fully describes the output
- supporting: a message that may be used in conjunction with visual output

## See Also

- [init(LocalizedStringResource)](intentdialog/init(_:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(stringLiteral: String)](intentdialog/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: String.LocalizationValue.StringInterpolation)](intentdialog/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(full:supporting:))*