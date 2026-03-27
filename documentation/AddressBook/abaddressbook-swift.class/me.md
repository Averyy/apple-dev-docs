# me()

**Framework**: Address Book  
**Kind**: method

Returns the `ABPerson` record that represents the logged-in user.

**Availability**:
- macOS ?+

## Declaration

```swift
func me() -> ABPerson!
```

#### Return Value

The `ABPerson` record that represents the logged-in user.

#### Discussion

If the user never specified such a record, this method returns `nil`.

## See Also

- [func setMe(ABPerson!)](abaddressbook-swift.class/setme(_:).md)
  Sets the record that represents the logged-in user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/me())*