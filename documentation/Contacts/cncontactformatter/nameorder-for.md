# nameOrder(for:)

**Framework**: Contacts  
**Kind**: method

Returns the display name order.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func nameOrder(for contact: CNContact) -> CNContactDisplayNameOrder
```

#### Return Value

The display order to use when combining the given name and family name components.

#### Discussion

For more information about display name orders, see [`CNContactDisplayNameOrder`](cncontactdisplaynameorder.md).

## Parameters

- `contact`: The contact whose name is to be formatted.

## See Also

- [class func delimiter(for: CNContact) -> String](cncontactformatter/delimiter(for:).md)
  Returns the delimiter to use between name components.
- [enum CNContactDisplayNameOrder](cncontactdisplaynameorder.md)
  The formatting orders for contact names component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/nameorder(for:))*