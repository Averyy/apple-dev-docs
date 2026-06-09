# presentMerchandising(_:from:)

**Framework**: StoreKit  
**Kind**: method

Display a merchandising view.

**Availability**:
- macOS 26.2+

## Declaration

```swift
@MainActor
static func presentMerchandising(_ kind: AppStoreMerchandisingKind, from window: NSWindow) async throws -> AppStoreMerchandisingKind.PresentationResult
```

#### Return Value

The result of the App Store merchandising presentation.

#### Discussion

> **Note**: A `StoreKitError`.

## Parameters

- `kind`: The merchandising kind to merchandise.
- `window`: The view window to show the merchandising UI in proximity to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmerchandising(_:from:)-8bblo)*