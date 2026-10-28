# displayedPerson

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optional. Specifies the person properties that the new-person view controller pre-fills in its views.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`contact`](../../ContactsUI/cncontactviewcontroller/contact.md) instead.

## Declaration

```swift
var displayedPerson: ABRecord? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) ABRecordRef displayedPerson;
```

## Discussion

When this property has no person properties, the new-person view controller does not pre-fill properties in its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/displayedperson)*