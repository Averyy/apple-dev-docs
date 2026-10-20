# contact

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The contact being displayed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var contact: CNContact { get }
```

*macOS*

```swift
@NSCopying
var contact: CNContact? { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, strong, readonly) CNContact * contact;
```

*macOS*

```objc
@property (copy, readwrite, nullable) CNContact * contact;
```

## See Also

### Displaying Contact Properties
- [var alternateName: String?](./alternatename.md)
  The name to use if the contact has no display name.
- [var message: String?](./message.md)
  The message displayed under the name of the contact.
- [var displayedPropertyKeys: [Any]?](./displayedpropertykeys.md)
  The contact property keys to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/contact)*