# CNPostalAddressPropertyAttribute

**Framework**: Contacts  
**Kind**: var  
**Role**: Global Variable

An attribute that identifies the purpose of a range of characters in an attributed string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CNPostalAddressPropertyAttribute: String
```

```c
extern NSString * const CNPostalAddressPropertyAttribute;
```

## Discussion

The value of this key is a string constant that specifies the meaning of the range of characters. For example, the value is [`CNPostalAddressCityKey`](./cnpostaladdresscitykey.md) when the characters specify the city portion of the address.

## See Also

### Generating a formatted attributed string
- [func attributedString(from: CNPostalAddress, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](./cnpostaladdressformatter/attributedstring%28from,withdefaultattributes%29.md)
  Returns a formatted postal address as an attributed string.
- [class func attributedString(from: CNPostalAddress, style: CNPostalAddressFormatterStyle, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](./cnpostaladdressformatter/attributedstring%28from,style,withdefaultattributes%29.md)
  Returns a postal address as an attributed string and formatted for the specified style.
- [let CNPostalAddressLocalizedPropertyNameAttribute: String](./cnpostaladdresslocalizedpropertynameattribute.md)
  An attribute that identifies the localized property of postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdresspropertyattribute)*