# defaultCountryCode()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the default country code for records with unspecified country codes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func defaultCountryCode() -> String!
```

```objc
- (NSString *) defaultCountryCode;
```

## Return Value

The default country code.

## Discussion

This value returned is set by the user in the Address Book application’s general preference. The supported country codes are listed in [`ABPerson`](../abperson.md).

## See Also

### Retrieving Default Values
- [func defaultNameOrdering() -> Int](./defaultnameordering%28%29.md)
  Returns the default name ordering defined by the user in the Address Book application’s preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/defaultcountrycode())*