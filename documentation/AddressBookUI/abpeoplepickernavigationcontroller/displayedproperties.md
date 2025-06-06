# displayedProperties

**Framework**: Address Book UI  
**Kind**: property

The properties (such as name or telephone number) the picker displays when it shows a person.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var displayedProperties: [NSNumber]? { get set }
```

#### Discussion

Objects in the array are instances of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that represent [`ABPropertyID`](https://developer.apple.com/documentation/AddressBook/ABPropertyID) values.

The name property is always displayed if available.

To have the picker display a single property for the person displayed, such as the telephone number, set `displayedProperties` to an array with a single value, such as `kABPersonPhoneProperty`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/displayedproperties)*