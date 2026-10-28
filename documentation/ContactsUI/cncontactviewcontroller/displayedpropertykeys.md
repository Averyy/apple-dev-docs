# displayedPropertyKeys

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The contact property keys to display.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var displayedPropertyKeys: [Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray * displayedPropertyKeys;
```

## Discussion

If this property is not set, the view controller displays all properties.

## See Also

### Displaying Contact Properties
- [var contact: CNContact](./contact.md)
  The contact being displayed.
- [var alternateName: String?](./alternatename.md)
  The name to use if the contact has no display name.
- [var message: String?](./message.md)
  The message displayed under the name of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/displayedpropertykeys)*