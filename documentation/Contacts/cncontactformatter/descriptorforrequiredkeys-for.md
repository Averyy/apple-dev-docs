# descriptorForRequiredKeys(for:)

**Framework**: Contacts  
**Kind**: method

Returns the required key descriptor for the specified formatting style of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func descriptorForRequiredKeys(for style: CNContactFormatterStyle) -> any CNKeyDescriptor
```

#### Return Value

The contact key descriptor for the formatting style.

#### Discussion

Include this method with the keys to fetch when fetching contacts. To format multiple styles, you can include multiple key descriptors with the keys to fetch.

## Parameters

- `style`: The formatting style to be used for contact name.

## See Also

- [class var descriptorForRequiredKeysForDelimiter: any CNKeyDescriptor](cncontactformatter/descriptorforrequiredkeysfordelimiter.md)
  Returns the required key descriptor for the name delimiter.
- [class var descriptorForRequiredKeysForNameOrder: any CNKeyDescriptor](cncontactformatter/descriptorforrequiredkeysfornameorder.md)
  Returns the required key descriptor for the display name order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/descriptorforrequiredkeys(for:))*