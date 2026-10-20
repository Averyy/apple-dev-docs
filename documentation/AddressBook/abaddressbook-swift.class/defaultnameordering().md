# defaultNameOrdering()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the default name ordering defined by the user in the Address Book application’s preferences.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func defaultNameOrdering() -> Int
```

```objc
- (NSInteger) defaultNameOrdering;
```

#### Return Value

The default name ordering defined by the user in the Address Book application’s preferences.

#### Discussion

The possible values are kABFirstNameFirst and kABLastNameFirst.

## See Also

### Retrieving Default Values
- [func defaultCountryCode() -> String!](./defaultcountrycode%28%29.md)
  Returns the default country code for records with unspecified country codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/defaultnameordering())*