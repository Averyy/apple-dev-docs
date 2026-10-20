# ABRecord

**Framework**: EventKit  
**Kind**: typealias  
**Role**: Type Alias

A reference to an ABRecord object or any of its derivedopaque types.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: use CNContact, CNGroup, or CNContainer

## Declaration

```swift
typealias ABRecord = CFTypeRef
```

```c
typedef CFTypeRef ABRecordRef;
```

## See Also

### Finding Participant Address Book Records
- [func abRecord(with: ABAddressBook) -> ABRecord?](./ekparticipant/abrecord%28with%29.md)
  Returns the address book record that represents the participant.
- [func abPerson(in: ABAddressBook) -> ABPerson?](./ekparticipant/abperson%28in%29.md)
  Returns the address book record that represents the participant.
- [typealias ABAddressBook](./abaddressbook.md)
  A reference to an ABAddressBook object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/abrecord)*