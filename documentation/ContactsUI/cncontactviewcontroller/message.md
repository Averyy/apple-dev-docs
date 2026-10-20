# message

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The message displayed under the name of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var message: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * message;
```

## See Also

### Displaying Contact Properties
- [var contact: CNContact](./contact.md)
  The contact being displayed.
- [var alternateName: String?](./alternatename.md)
  The name to use if the contact has no display name.
- [var displayedPropertyKeys: [Any]?](./displayedpropertykeys.md)
  The contact property keys to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/message)*