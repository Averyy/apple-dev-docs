# deleteHistory(during:)

**Framework**: Screen Time  
**Kind**: method

Deletes web history that occurred during the date interval you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func deleteHistory(during interval: DateInterval)
```

## Parameters

- `interval`: The date interval of web history you want to delete.

## See Also

- [func deleteAllHistory()](stwebhistory/deleteallhistory.md)
  Deletes all web history associated with the bundle identifier you specified during initialization.
- [func deleteHistory(for: URL)](stwebhistory/deletehistory(for:).md)
  Deletes all the web history for the URL you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/deletehistory(during:))*