# CNContactDisplayNameOrder

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CNContactDisplayNameOrder : NSInteger;
```

## Topics

### Constants
- [CNContactDisplayNameOrder.userDefault](./cncontactdisplaynameorder/userdefault.md)
  Display name order by user default.
- [CNContactDisplayNameOrder.givenNameFirst](./cncontactdisplaynameorder/givennamefirst.md)
  Display name order by given name first.
- [CNContactDisplayNameOrder.familyNameFirst](./cncontactdisplaynameorder/familynamefirst.md)
  Display name order by family name first.
### Initializers
- [init?(rawValue: Int)](./cncontactdisplaynameorder/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting format information
- [class func delimiter(for: CNContact) -> String](./cncontactformatter/delimiter%28for%29.md)
  Returns the delimiter to use between name components.
- [class func nameOrder(for: CNContact) -> CNContactDisplayNameOrder](./cncontactformatter/nameorder%28for%29.md)
  Returns the display name order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactdisplaynameorder)*