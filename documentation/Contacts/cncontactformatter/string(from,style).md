# string(from:style:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) stringFromContact:(CNContact *) contact style:(CNContactFormatterStyle) style;
```

#### Return Value

The formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.
- `style`: The formatting style to be used for the contact name.

## See Also

### Creating a formatted string
- [func string(from: CNContact) -> String?](./string%28from%29.md)
  Formats the contact name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/string(from:style:))*