# me()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the `ABPerson` record that represents the logged-in user.

**Availability**:
- macOS

## Declaration

```swift
func me() -> ABPerson!
```

```objc
- (ABPerson *) me;
```

## Return Value

The `ABPerson` record that represents the logged-in user.

## Discussion

If the user never specified such a record, this method returns `nil`.

## See Also

### Setting and Retrieving the Logged-in User’s Record
- [func setMe(ABPerson!)](./setme%28_%29.md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/me())*