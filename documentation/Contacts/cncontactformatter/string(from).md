# string(from:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) stringFromContact:(CNContact *) contact;
```

#### Return Value

The formatted contact name.

## Parameters

- `contact`: The contact whose name is to be formatted.

## See Also

### Creating a formatted string
- [class func string(from: CNContact, style: CNContactFormatterStyle) -> String?](./string%28from,style%29.md)
  Returns the contact name, formatted with the specified formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/string(from:))*