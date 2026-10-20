# uniqueId

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

Returns the unique ID for a record.

**Availability**:
- macOS

## Declaration

```swift
var uniqueId: String! { get }
```

```objc
@property (copy, readonly) NSString * uniqueId;
```

#### Return Value

The unique ID.

#### Discussion

This method is equivalent to invoking [`value(forProperty:)`](./value%28forproperty%29.md), passing `kABUIDProperty` as the argument.

## See Also

### Getting Identifying Information
- [var displayName: String!](./displayname.md)
  A user-visible string representing the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/uniqueid)*