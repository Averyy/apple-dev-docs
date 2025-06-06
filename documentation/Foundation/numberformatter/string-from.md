# string(from:)

**Framework**: Foundation  
**Kind**: method

Returns a string containing the formatted value of the provided number object.

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
func string(from number: NSNumber) -> String?
```

#### Return Value

A string containing the formatted value of `number` using the receiver’s current settings.

## Parameters

- `number`: An   object that is parsed to create the returned string object.

## See Also

- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](numberformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func number(from: String) -> NSNumber?](numberformatter/number(from:).md)
  Returns an [`NSNumber`](nsnumber.md) object created by parsing a given string.
- [class func localizedString(from: NSNumber, number: NumberFormatter.Style) -> String](numberformatter/localizedstring(from:number:).md)
  Returns a localized number string with the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/string(from:))*