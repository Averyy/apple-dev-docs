# string(from:style:)

**Framework**: Contacts  
**Kind**: method

Returns the contact name, formatted with the specified formatter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func string(from contact: CNContact, style: CNContactFormatterStyle) -> String?
```

#### Return Value

The formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.
- `style`: The formatting style to be used for the contact name.

## See Also

- [func string(from: CNContact) -> String?](cncontactformatter/string(from:).md)
  Formats the contact name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/string(from:style:))*