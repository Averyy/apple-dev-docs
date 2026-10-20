# token(for:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Returns an external purchase token of the specified type.

**Availability**:
- iOS 18.1+ - Deprecated in 27.2
- iPadOS 18.1+ - Deprecated in 27.2
- Mac Catalyst 18.1+ - Deprecated in 27.2
- macOS 15.1+ - Deprecated in 27.2
- tvOS 18.1+ - Deprecated in 27.2
- visionOS 2.1+ - Deprecated in 27.2
- watchOS 11.1+ - Deprecated in 27.2

> **Deprecated**: Use `token(for:)` with a `TokenType` instead.

## Declaration

```swift
static func token(for tokenType: String) async throws -> ExternalPurchaseCustomLink.Token?
```

#### Discussion

If `isEligible` is `false`, this method will always fail.

> **Throws**: A `StoreKitError`.

## Parameters

- `tokenType`: The type of token to request.

## See Also

### Deprecated methods and values
- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](./shownotice%28type%29.md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeType](./noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token(for:)-1fyo)*