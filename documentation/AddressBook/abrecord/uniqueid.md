# uniqueId

**Framework**: Address Book  
**Kind**: property

Returns the unique ID for a record.

**Availability**:
- macOS ?+

## Declaration

```swift
var uniqueId: String! { get }
```

#### Return Value

The unique ID.

#### Discussion

This method is equivalent to invoking [`value(forProperty:)`](abrecord/value(forproperty:).md), passing `kABUIDProperty` as the argument.

## See Also

- [var displayName: String!](abrecord/displayname.md)
  A user-visible string representing the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord/uniqueid)*