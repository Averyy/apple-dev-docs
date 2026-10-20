# attributedString(from:defaultAttributes:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSAttributedString *) attributedStringFromContact:(CNContact *) contact defaultAttributes:(NSDictionary *) attributes;
```

#### Return Value

The formatted contact name as an attributed string.

#### Discussion

This method behaves similarly to [`string(from:style:)`](./string%28from,style%29.md), except that it returns an attributed string. It includes the attribute key [`CNContactPropertyAttribute`](../cncontactpropertyattribute.md) whose attribute values are contact property keys, such as [`CNContactGivenNameKey`](../cncontactgivennamekey.md). This identifies the name components in the formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.
- `attributes`: The default attributes to use. For more information, see [`Formatter`](../../Foundation/formatter.md).

## See Also

### Creating a formatted attributed string
- [class func attributedString(from: CNContact, style: CNContactFormatterStyle, defaultAttributes: [AnyHashable : Any]?) -> NSAttributedString?](./attributedstring%28from,style,defaultattributes%29.md)
  Formats the contact name as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/attributedstring(from:defaultattributes:))*