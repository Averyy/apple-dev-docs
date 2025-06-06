# attributedString(from:withDefaultAttributes:)

**Framework**: Contacts  
**Kind**: method

Returns a formatted postal address as an attributed string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func attributedString(from postalAddress: CNPostalAddress, withDefaultAttributes attributes: [AnyHashable : Any] = [:]) -> NSAttributedString
```

#### Return Value

The formatted postal address as an attributed string.

#### Discussion

This method behaves similarly to  [`string(from:)`](cnpostaladdressformatter/string(from:).md), except that it returns an attributed string. It includes the attribute key [`CNPostalAddressPropertyAttribute`](cnpostaladdresspropertyattribute.md), whose attribute values are postal address property keys, such as [`CNPostalAddressStreetKey`](cnpostaladdressstreetkey.md). This identifies the postal address components in the formatted postal address. It also includes the attribute key [`CNPostalAddressLocalizedPropertyNameAttribute`](cnpostaladdresslocalizedpropertynameattribute.md) whose attribute values are the localized strings for the postal address property keys.

## Parameters

- `postalAddress`: The postal address to format.
- `attributes`: The default attributes to use. You can specify the   or   attributes.

## See Also

- [class func attributedString(from: CNPostalAddress, style: CNPostalAddressFormatterStyle, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](cnpostaladdressformatter/attributedstring(from:style:withdefaultattributes:).md)
  Returns a postal address as an attributed string and formatted for the specified style.
- [let CNPostalAddressPropertyAttribute: String](cnpostaladdresspropertyattribute.md)
  An attribute that identifies the purpose of a range of characters in an attributed string.
- [let CNPostalAddressLocalizedPropertyNameAttribute: String](cnpostaladdresslocalizedpropertynameattribute.md)
  An attribute that identifies the localized property of postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter/attributedstring(from:withdefaultattributes:))*