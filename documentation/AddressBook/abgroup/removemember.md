# removeMember(_:)

**Framework**: Address Book  
**Kind**: method

Removes a person from a group.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeMember(_ person: ABPerson!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the `person` argument is not in the group, this method does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false). If `person` is `nil`, this method raises an exception.

## Parameters

- `person`: The person to be removed.

## See Also

- [func addMember(ABPerson!) -> Bool](abgroup/addmember(_:).md)
  Adds a person to a group.
- [func members() -> [Any]!](abgroup/members.md)
  Returns an array of persons in a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/removemember(_:))*