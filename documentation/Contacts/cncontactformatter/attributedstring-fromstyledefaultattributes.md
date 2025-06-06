# attributedString(from:style:defaultAttributes:)

**Framework**: Contacts  
**Kind**: method

Formats the contact name as an attributed string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func attributedString(from contact: CNContact, style: CNContactFormatterStyle, defaultAttributes attributes: [AnyHashable : Any]? = nil) -> NSAttributedString?
```

#### Return Value

The formatted contact name as an attributed string.

#### Discussion

This method behaves similarly to [`string(from:style:)`](cncontactformatter/string(from:style:).md), except that it returns an attributed string. It includes the attribute key [`CNContactPropertyAttribute`](cncontactpropertyattribute.md), whose attribute values are contact property keys, such as [`CNContactGivenNameKey`](cncontactgivennamekey.md). This identifies the name components in the formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.
- `style`: The formatting style to be used for the contact name.
- `attributes`: The default attributes to use. For more information, see  .

## See Also

- [func attributedString(from: CNContact, defaultAttributes: [AnyHashable : Any]?) -> NSAttributedString?](cncontactformatter/attributedstring(from:defaultattributes:).md)
  Formats the contact name as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/attributedstring(from:style:defaultattributes:))*