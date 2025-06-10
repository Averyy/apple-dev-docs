# setMe(_:)

**Framework**: Address Book  
**Kind**: method

Sets the record that represents the logged-in user.

**Availability**:
- macOS ?+

## Declaration

```swift
func setMe(_ moi: ABPerson!)
```

#### Discussion

If you don’t want a record to represent the logged-in user, then pass `nil` as the `person` argument. Note that this will not delete the existing record, if one is set.

## Parameters

- `moi`: The person to set as representing the logged-in user.

## See Also

- [func me() -> ABPerson!](abaddressbook/me.md)
  Returns the `ABPerson` record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/setme(_:))*