# requestDeletion(in:)

**Framework**: MarketplaceKit  
**Kind**: method

Prompts the person to delete the app.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
@MainActor
final func requestDeletion(in scene: UIWindowScene) async throws
```

#### Discussion

This method presents a system confirmation for the person to permit or deny the app’s deletion.

## Parameters

- `scene`: The window scene in which to present app-deletion confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/requestdeletion(in:))*