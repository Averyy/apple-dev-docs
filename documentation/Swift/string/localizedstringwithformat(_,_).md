# localizedStringWithFormat(_:_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func localizedStringWithFormat(_ format: String, _ arguments: any CVarArg...) -> String
```

## See Also

### Creating a String Using Formats
- [init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format: String, arguments: [any CVarArg])](./init%28format,arguments%29.md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format: String, locale: Locale?, any CVarArg...)](./init%28format,locale,_%29.md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format: String, locale: Locale?, arguments: [any CVarArg])](./init%28format,locale,arguments%29.md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizedstringwithformat(_:_:))*