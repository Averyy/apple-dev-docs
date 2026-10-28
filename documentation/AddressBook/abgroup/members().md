# members()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array of persons in a group.

**Availability**:
- macOS

## Declaration

```swift
func members() -> [Any]!
```

```objc
- (NSArray *) members;
```

## Discussion

If this group doesn’t contain any people, this method returns an empty array.

## See Also

### Managing persons
- [func addMember(ABPerson!) -> Bool](./addmember%28_%29.md)
  Adds a person to a group.
- [func removeMember(ABPerson!) -> Bool](./removemember%28_%29.md)
  Removes a person from a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/members())*