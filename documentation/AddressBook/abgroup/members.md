# members()

**Framework**: Address Book  
**Kind**: method

Returns an array of persons in a group.

**Availability**:
- macOS ?+

## Declaration

```swift
func members() -> [Any]!
```

#### Discussion

If this group doesn’t contain any people, this method returns an empty array.

## See Also

- [func addMember(ABPerson!) -> Bool](abgroup/addmember(_:).md)
  Adds a person to a group.
- [func removeMember(ABPerson!) -> Bool](abgroup/removemember(_:).md)
  Removes a person from a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/members())*