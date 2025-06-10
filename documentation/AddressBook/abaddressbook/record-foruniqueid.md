# record(forUniqueId:)

**Framework**: Address Book  
**Kind**: method

Returns the person or group record that matches the given unique ID.

**Availability**:
- macOS ?+

## Declaration

```swift
func record(forUniqueId uniqueId: String!) -> ABRecord!
```

#### Return Value

The person or group record that matches the given unique ID.

#### Discussion

If no record has the given ID, this method returns `nil`.

## Parameters

- `uniqueId`: The unique ID of the record. This value must not be  ; otherwise, an exception is raised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/record(foruniqueid:))*