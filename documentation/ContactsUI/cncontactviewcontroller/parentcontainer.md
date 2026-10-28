# parentContainer

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The container in which to add a new contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var parentContainer: CNContainer? { get set }
```

```objc
@property (nonatomic, strong, nullable) CNContainer * parentContainer;
```

## Discussion

If you do not set this property, the view controller adds a new contact to the default container.

## See Also

### Configuring the Contact’s Relationships
- [var parentGroup: CNGroup?](./parentgroup.md)
  The group in which to add a new contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/parentcontainer)*