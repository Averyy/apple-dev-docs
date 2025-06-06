# abRecord(with:)

**Framework**: EventKit  
**Kind**: method

Returns the address book record that represents the participant.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func abRecord(with addressBook: ABAddressBook) -> ABRecord?
```

#### Return Value

The address book record for the participant, or `nil` if the record is not found.

#### Discussion

This method searches for a record match based on the participant’s email address.

##### Special Considerations

> **Note**:  This instance method is only available on iOS. For macOS, see the [`abPerson(in:)`](ekparticipant/abperson(in:).md) instance method.

 This instance method is only available on iOS. For macOS, see the [`abPerson(in:)`](ekparticipant/abperson(in:).md) instance method.

## Parameters

- `addressBook`: The address book to search.

## See Also

- [func abPerson(in: ABAddressBook) -> ABPerson?](ekparticipant/abperson(in:).md)
  Returns the address book record that represents the participant.
- [typealias ABAddressBook](abaddressbook.md)
  A reference to an ABAddressBook object.
- [typealias ABRecord](abrecord.md)
  A reference to an ABRecord object or any of its derivedopaque types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/abrecord(with:))*