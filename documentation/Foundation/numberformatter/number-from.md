# number(from:)

**Framework**: Foundation  
**Kind**: method

Returns an [`NSNumber`](nsnumber.md) object created by parsing a given string.

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
func number(from string: String) -> NSNumber?
```

#### Return Value

An [`NSNumber`](nsnumber.md) object created by parsing `string` using the receiver’s format, or `nil` if no single number could be parsed.

#### Discussion

If a string contains any characters other than numerical digits or locale-appropriate group or decimal separators, parsing will fail.

Any leading or trailing space separator characters in a string are ignored. For example, the strings “ 5”, “5 “, and “5” all produce the number `5`.

## Parameters

- `string`: An   object that is parsed to generate the returned number object.

## See Also

- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](numberformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func string(from: NSNumber) -> String?](numberformatter/string(from:).md)
  Returns a string containing the formatted value of the provided number object.
- [class func localizedString(from: NSNumber, number: NumberFormatter.Style) -> String](numberformatter/localizedstring(from:number:).md)
  Returns a localized number string with the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/number(from:))*