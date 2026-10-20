# people()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array of all the people in the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
func people() -> [Any]!
```

```objc
- (NSArray *) people;
```

#### Return Value

An array of all the people in the Address Book database.

#### Discussion

If the database doesn’t contain any people, this method returns an empty array.

## See Also

### Retrieving Groups and People
- [func groups() -> [Any]!](./groups%28%29.md)
  Returns an array of all the groups in the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/people())*