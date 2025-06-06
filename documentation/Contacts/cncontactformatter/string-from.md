# string(from:)

**Framework**: Contacts  
**Kind**: method

Formats the contact name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(from contact: CNContact) -> String?
```

#### Return Value

The formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.

## See Also

- [class func string(from: CNContact, style: CNContactFormatterStyle) -> String?](cncontactformatter/string(from:style:).md)
  Returns the contact name, formatted with the specified formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/string(from:))*