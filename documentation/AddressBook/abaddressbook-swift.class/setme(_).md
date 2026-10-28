# setMe(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Sets the record that represents the logged-in user.

**Availability**:
- macOS

## Declaration

```swift
func setMe(_ moi: ABPerson!)
```

```objc
- (void) setMe:(ABPerson *) moi;
```

## Discussion

If you don’t want a record to represent the logged-in user, then pass `nil` as the `person` argument. Note that this will not delete the existing record, if one is set.

## Parameters

- `moi`: The person to set as representing the logged-in user.

## See Also

### Setting and Retrieving the Logged-in User’s Record
- [func me() -> ABPerson!](./me%28%29.md)
  Returns the `ABPerson` record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/setme(_:))*