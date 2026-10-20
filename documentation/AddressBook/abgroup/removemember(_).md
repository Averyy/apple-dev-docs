# removeMember(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes a person from a group.

**Availability**:
- macOS

## Declaration

```swift
func removeMember(_ person: ABPerson!) -> Bool
```

```objc
- (BOOL) removeMember:(ABPerson *) person;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If the `person` argument is not in the group, this method does nothing and returns [`false`](../../Swift/false.md). If `person` is `nil`, this method raises an exception.

## Parameters

- `person`: The person to be removed.

## See Also

### Managing persons
- [func addMember(ABPerson!) -> Bool](./addmember%28_%29.md)
  Adds a person to a group.
- [func members() -> [Any]!](./members%28%29.md)
  Returns an array of persons in a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/removemember(_:))*