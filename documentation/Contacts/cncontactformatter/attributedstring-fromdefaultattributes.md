# attributedString(from:defaultAttributes:)

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
func attributedString(from contact: CNContact, defaultAttributes attributes: [AnyHashable : Any]? = nil) -> NSAttributedString?
```

#### Return Value

The formatted contact name as an attributed string.

#### Discussion

This method behaves similarly to [`string(from:style:)`](cncontactformatter/string(from:style:).md), except that it returns an attributed string. It includes the attribute key [`CNContactPropertyAttribute`](cncontactpropertyattribute.md) whose attribute values are contact property keys, such as [`CNContactGivenNameKey`](cncontactgivennamekey.md). This identifies the name components in the formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.
- `attributes`: The default attributes to use. For more information, see  .

## See Also

- [class func attributedString(from: CNContact, style: CNContactFormatterStyle, defaultAttributes: [AnyHashable : Any]?) -> NSAttributedString?](cncontactformatter/attributedstring(from:style:defaultattributes:).md)
  Formats the contact name as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/attributedstring(from:defaultattributes:))*