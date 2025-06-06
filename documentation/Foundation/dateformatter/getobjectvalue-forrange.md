# getObjectValue(_:for:range:)

**Framework**: Foundation  
**Kind**: method

Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, range rangep: UnsafeMutablePointer<NSRange>?) throws
```

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `obj`: If the receiver is able to parse  , upon return contains a date representation of  .
- `string`: The string to parse.
- `rangep`: If the receiver is able to parse  , upon return contains the range of   used to create the date.

## See Also

- [func string(for: Any?) -> String?](formatter/string(for:).md)
  The default implementation of this method raises an exception.
- [func date(from: String) -> Date?](dateformatter/date(from:).md)
  Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [func string(from: Date) -> String](dateformatter/string(from:).md)
  Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [class func localizedString(from: Date, dateStyle: DateFormatter.Style, timeStyle: DateFormatter.Style) -> String](dateformatter/localizedstring(from:datestyle:timestyle:).md)
  Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/getobjectvalue(_:for:range:))*