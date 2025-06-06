# init(format:locale:arguments:)

**Framework**: Swift  
**Kind**: init

Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.

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
init(format: String, locale: Locale?, arguments: [any CVarArg])
```

## See Also

- [init(format: String, any CVarArg...)](string/init(format:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format: String, arguments: [any CVarArg])](string/init(format:arguments:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format: String, locale: Locale?, any CVarArg...)](string/init(format:locale:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [static func localizedStringWithFormat(String, any CVarArg...) -> String](string/localizedstringwithformat(_:_:).md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(format:locale:arguments:))*