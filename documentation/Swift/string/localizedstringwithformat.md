# localizedStringWithFormat(_:_:)

**Framework**: Swift  
**Kind**: method

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

- [init(format: String, any CVarArg...)](string/init(format:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format: String, arguments: [any CVarArg])](string/init(format:arguments:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format: String, locale: Locale?, any CVarArg...)](string/init(format:locale:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format: String, locale: Locale?, arguments: [any CVarArg])](string/init(format:locale:arguments:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizedstringwithformat(_:_:))*