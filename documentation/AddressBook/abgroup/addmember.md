# addMember(_:)

**Framework**: Address Book  
**Kind**: method

Adds a person to a group.

**Availability**:
- macOS ?+

## Declaration

```swift
func addMember(_ person: ABPerson!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the `person` argument is already part of the group, this method does nothing and returns [`true`](https://developer.apple.com/documentation/swift/true). If the `person` argument is `nil`, this method raises an exception.

##### Special Considerations

Prior to OS X v10.6, if the person record is already in the group, this method does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `person`: The person record to be added.

## See Also

- [func removeMember(ABPerson!) -> Bool](abgroup/removemember(_:).md)
  Removes a person from a group.
- [func members() -> [Any]!](abgroup/members.md)
  Returns an array of persons in a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/addmember(_:))*