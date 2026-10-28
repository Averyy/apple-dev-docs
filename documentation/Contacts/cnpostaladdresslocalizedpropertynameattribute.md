# CNPostalAddressLocalizedPropertyNameAttribute

**Framework**: Contacts  
**Kind**: var  
**Role**: Global Variable

An attribute that identifies the localized property of postal address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CNPostalAddressLocalizedPropertyNameAttribute: String
```

```c
extern NSString * const CNPostalAddressLocalizedPropertyNameAttribute;
```

## Discussion

This constant is a key in the attributed string whose value is a localized version of the CNPostalAddress property key. This label takes a string value.

## See Also

### Generating a formatted attributed string
- [func attributedString(from: CNPostalAddress, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](./cnpostaladdressformatter/attributedstring%28from,withdefaultattributes%29.md)
  Returns a formatted postal address as an attributed string.
- [class func attributedString(from: CNPostalAddress, style: CNPostalAddressFormatterStyle, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](./cnpostaladdressformatter/attributedstring%28from,style,withdefaultattributes%29.md)
  Returns a postal address as an attributed string and formatted for the specified style.
- [let CNPostalAddressPropertyAttribute: String](./cnpostaladdresspropertyattribute.md)
  An attribute that identifies the purpose of a range of characters in an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdresslocalizedpropertynameattribute)*