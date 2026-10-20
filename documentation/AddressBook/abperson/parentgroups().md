# parentGroups()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array of the address book groups that this person belongs to.

**Availability**:
- macOS

## Declaration

```swift
func parentGroups() -> [Any]!
```

```objc
- (NSArray *) parentGroups;
```

#### Discussion

If the person doesn’t belong to any groups, this method returns an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/parentgroups())*