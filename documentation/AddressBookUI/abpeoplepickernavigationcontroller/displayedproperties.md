# displayedProperties

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The properties (such as name or telephone number) the picker displays when it shows a person.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactPickerViewController`](../../ContactsUI/cncontactpickerviewcontroller.md) instead.

## Declaration

```swift
var displayedProperties: [NSNumber]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSNumber *> * displayedProperties;
```

#### Discussion

Objects in the array are instances of [`NSNumber`](../../Foundation/nsnumber.md) that represent [`ABPropertyID`](../../AddressBook/abpropertyid.md) values.

The name property is always displayed if available.

To have the picker display a single property for the person displayed, such as the telephone number, set `displayedProperties` to an array with a single value, such as `kABPersonPhoneProperty`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/displayedproperties)*