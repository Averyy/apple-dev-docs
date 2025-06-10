# CNContactDisplayNameOrder

**Framework**: Contacts  
**Kind**: enum

The formatting orders for contact names component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNContactDisplayNameOrder
```

## Topics

### Constants
- [CNContactDisplayNameOrder.userDefault](cncontactdisplaynameorder/userdefault.md)
  Display name order by user default.
- [CNContactDisplayNameOrder.givenNameFirst](cncontactdisplaynameorder/givennamefirst.md)
  Display name order by given name first.
- [CNContactDisplayNameOrder.familyNameFirst](cncontactdisplaynameorder/familynamefirst.md)
  Display name order by family name first.
### Initializers
- [init?(rawValue: Int)](cncontactdisplaynameorder/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func delimiter(for: CNContact) -> String](cncontactformatter/delimiter(for:).md)
  Returns the delimiter to use between name components.
- [class func nameOrder(for: CNContact) -> CNContactDisplayNameOrder](cncontactformatter/nameorder(for:).md)
  Returns the display name order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactdisplaynameorder)*