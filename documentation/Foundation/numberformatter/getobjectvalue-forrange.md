# getObjectValue(_:for:range:)

**Framework**: Foundation  
**Kind**: method

Returns by reference a cell-content object after creating it from a range of characters in a given string.

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

If a string contains any characters other than numerical digits or locale-appropriate group or decimal separators, parsing will fail.

Any leading or trailing space separator characters in a string are ignored. For example, the strings “ 5”, “5 “, and “5” all produce the number `5`.

If there is an error, this method calls `control(_:didFailToFormatString:errorDescription:)` on the delegate.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `obj`: On return, contains an instance of   or   based on the current value of the   property. Returns   by reference if conversion failed.
- `string`: A string object with the range of characters specified in   that is used to create  .
- `rangep`: A range of characters in  . On return, contains the actual range of characters used to create the object.

## See Also

- [func number(from: String) -> NSNumber?](numberformatter/number(from:).md)
  Returns an [`NSNumber`](nsnumber.md) object created by parsing a given string.
- [func string(from: NSNumber) -> String?](numberformatter/string(from:).md)
  Returns a string containing the formatted value of the provided number object.
- [class func localizedString(from: NSNumber, number: NumberFormatter.Style) -> String](numberformatter/localizedstring(from:number:).md)
  Returns a localized number string with the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/getobjectvalue(_:for:range:))*