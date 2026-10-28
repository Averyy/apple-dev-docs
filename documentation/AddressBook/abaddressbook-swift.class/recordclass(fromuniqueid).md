# recordClass(fromUniqueId:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the class name of the record that matches the given unique ID.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func recordClass(fromUniqueId uniqueId: String!) -> String!
```

```objc
- (NSString *) recordClassFromUniqueId:(NSString *) uniqueId;
```

## Return Value

The name of the class of the record, for example `ABPerson`.

## Parameters

- `uniqueId`: The unique ID of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/recordclass(fromuniqueid:))*