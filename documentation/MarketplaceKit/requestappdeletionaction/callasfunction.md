# callAsFunction(_:)

**Framework**: MarketplaceKit  
**Kind**: method

Requests deletion of the specified app with someone’s confirmation.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func callAsFunction(_ app: AppLibrary.App) async throws
```

#### Discussion

When you call this action, the system presents a confirmation UI. If the person confirms, the system deletes the app and its data.

## Parameters

- `app`: The app to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/requestappdeletionaction/callasfunction(_:))*