# delimiter(for:)

**Framework**: Contacts  
**Kind**: method

Returns the delimiter to use between name components.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func delimiter(for contact: CNContact) -> String
```

#### Return Value

The delimiter to use between name components.

#### Discussion

If `contact` is `nil`, or if it has no first name, middle name, or last name, this method returns an empty string.

## Parameters

- `contact`: The contact whose name is to be formatted.

## See Also

- [class func nameOrder(for: CNContact) -> CNContactDisplayNameOrder](cncontactformatter/nameorder(for:).md)
  Returns the display name order.
- [enum CNContactDisplayNameOrder](cncontactdisplaynameorder.md)
  The formatting orders for contact names component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/delimiter(for:))*