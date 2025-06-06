# localizedString(from:number:)

**Framework**: Foundation  
**Kind**: method

Returns a localized number string with the specified style.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func localizedString(from num: NSNumber, number nstyle: NumberFormatter.Style) -> String
```

#### Return Value

An appropriately formatted `NSString`.

## Parameters

- `num`: The number to localize
- `nstyle`: The localization style to use. See   for the supported values.

## See Also

- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](numberformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func number(from: String) -> NSNumber?](numberformatter/number(from:).md)
  Returns an [`NSNumber`](nsnumber.md) object created by parsing a given string.
- [func string(from: NSNumber) -> String?](numberformatter/string(from:).md)
  Returns a string containing the formatted value of the provided number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/localizedstring(from:number:))*