# records(matching:)

**Framework**: Address Book  
**Kind**: method

Returns an array of records that match the given search element, or returns an empty array if no records match the search element.

**Availability**:
- macOS ?+

## Declaration

```swift
func records(matching search: ABSearchElement!) -> [Any]!
```

#### Return Value

An array of records that match the given search element, or an empty array if no records match the search element.

#### Discussion

If `search` is `nil`, this method raises an exception.

## Parameters

- `search`: The search element to perform the search against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/records(matching:))*