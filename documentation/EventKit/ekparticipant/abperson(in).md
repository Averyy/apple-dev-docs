# abPerson(in:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Returns the address book record that represents the participant.

**Availability**:
- macOS 10.8+ - Deprecated in 10.11

> **Deprecated**: Use contactPredicate instead

## Declaration

```swift
func abPerson(in addressBook: ABAddressBook) -> ABPerson?
```

```objc
- (ABPerson *) ABPersonInAddressBook:(ABAddressBook *) addressBook;
```

#### Return Value

The address book record for the participant, or `nil` if the record is not found.

#### Discussion

This method searches for a record match based on the participant’s email address.

##### Special Considerations

> **Note**:  This instance method is only available in macOS. For iOS, see the [`abRecord(with:)`](./abrecord%28with%29.md) instance method.

## Parameters

- `addressBook`: The address book to search.

## See Also

### Finding Participant Address Book Records
- [func abRecord(with: ABAddressBook) -> ABRecord?](./abrecord%28with%29.md)
  Returns the address book record that represents the participant.
- [typealias ABAddressBook](../abaddressbook.md)
  A reference to an ABAddressBook object.
- [typealias ABRecord](../abrecord.md)
  A reference to an ABRecord object or any of its derivedopaque types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/abperson(in:))*