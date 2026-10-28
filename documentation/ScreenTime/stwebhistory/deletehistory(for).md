# deleteHistory(for:)

**Framework**: Screen Time  
**Kind**: method  
**Role**: Instance Method

Deletes all the web history for the URL you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func deleteHistory(for url: URL)
```

```objc
- (void) deleteHistoryForURL:(NSURL *) url;
```

## Discussion

The framework references the entire URL to determine which web-usage data to delete.

## Parameters

- `url`: The URL associated with the web history to delete.

## See Also

### Instance methods
- [func deleteAllHistory()](./deleteallhistory%28%29.md)
  Deletes all web history associated with the bundle identifier you specified during initialization.
- [func deleteHistory(during: DateInterval)](./deletehistory%28during%29.md)
  Deletes web history that occurred during the date interval you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/deletehistory(for:))*