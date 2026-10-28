# addMember(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Adds a person to a group.

**Availability**:
- macOS

## Declaration

```swift
func addMember(_ person: ABPerson!) -> Bool
```

```objc
- (BOOL) addMember:(ABPerson *) person;
```

## Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the `person` argument is already part of the group, this method does nothing and returns [`true`](../../Swift/true.md). If the `person` argument is `nil`, this method raises an exception.

### Special Considerations

Prior to OS X v10.6, if the person record is already in the group, this method does nothing and returns [`false`](../../Swift/false.md).

## Parameters

- `person`: The person record to be added.

## See Also

### Managing persons
- [func removeMember(ABPerson!) -> Bool](./removemember%28_%29.md)
  Removes a person from a group.
- [func members() -> [Any]!](./members%28%29.md)
  Returns an array of persons in a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/addmember(_:))*