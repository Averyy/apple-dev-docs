# abPerson(in:)

**Framework**: Eventkit  
**Kind**: method

Returns the address book record that represents the participant.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func abPerson(in addressBook: ABAddressBook) -> ABPerson?
```

#### Return Value

The address book record for the participant, or `nil` if the record is not found.

#### Discussion

This method searches for a record match based on the participant’s email address.

##### Special Considerations

> **Note**:  This instance method is only available in macOS. For iOS, see the [`abRecord(with:)`](ekparticipant/abrecord(with:).md) instance method.

## Parameters

- `addressBook`: The address book to search.

## See Also

- [func abRecord(with: ABAddressBook) -> ABRecord?](ekparticipant/abrecord(with:).md)
  Returns the address book record that represents the participant.
- [typealias ABAddressBook](abaddressbook.md)
  A reference to an ABAddressBook object.
- [typealias ABRecord](abrecord.md)
  A reference to an ABRecord object or any of its derivedopaque types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/abperson(in:))*