# localizedString(from:number:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) localizedStringFromNumber:(NSNumber *) num numberStyle:(NSNumberFormatterStyle) nstyle;
```

#### Return Value

An appropriately formatted `NSString`.

## Parameters

- `num`: The number to localize
- `nstyle`: The localization style to use. See [`NumberFormatter.Style`](./style.md) for the supported values.

## See Also

### Converting Between Numbers and Strings
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](./getobjectvalue%28_,for,range%29.md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func number(from: String) -> NSNumber?](./number%28from%29.md)
  Returns an [`NSNumber`](../nsnumber.md) object created by parsing a given string.
- [func string(from: NSNumber) -> String?](./string%28from%29.md)
  Returns a string containing the formatted value of the provided number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/localizedstring(from:number:))*