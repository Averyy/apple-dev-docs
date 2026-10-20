# displayedPropertyKeys

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The [`CNContact`](../../Contacts/cncontact.md) property keys to display in the contact detail card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var displayedPropertyKeys: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * displayedPropertyKeys;
```

#### Discussion

All the properties of the contact are displayed if this property is not set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/displayedpropertykeys)*