# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) stringFromNumber:(NSNumber *) number;
```

#### Return Value

A string containing the formatted value of `number` using the receiver’s current settings.

## Parameters

- `number`: An [`NSNumber`](../nsnumber.md) object that is parsed to create the returned string object.

## See Also

### Converting Between Numbers and Strings
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](./getobjectvalue%28_,for,range%29.md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func number(from: String) -> NSNumber?](./number%28from%29.md)
  Returns an [`NSNumber`](../nsnumber.md) object created by parsing a given string.
- [class func localizedString(from: NSNumber, number: NumberFormatter.Style) -> String](./localizedstring%28from,number%29.md)
  Returns a localized number string with the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/string(from:))*