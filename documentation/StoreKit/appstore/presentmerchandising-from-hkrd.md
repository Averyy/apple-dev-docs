# presentMerchandising(_:from:)

**Framework**: StoreKit  
**Kind**: method

Display a merchandising view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
static func presentMerchandising(_ kind: AppStoreMerchandisingKind, from controller: UIViewController) async throws -> AppStoreMerchandisingKind.PresentationResult
```

#### Return Value

The result of the App Store merchandising presentation.

#### Discussion

> **Note**: A `StoreKitError`.

## Parameters

- `kind`: The merchandising kind to merchandise.
- `controller`: The view controller to show the merchandising UI in proximity to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmerchandising(_:from:)-hkrd)*