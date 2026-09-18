# ExternalPurchaseCustomLink.ExternalPurchaseType

**Framework**: StoreKit  
**Kind**: enum

Values that represent the types of external purchase an app can perform.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
enum ExternalPurchaseType
```

## Topics

### External purchase types
- [ExternalPurchaseCustomLink.ExternalPurchaseType.outOfApp(destinationURL:)](externalpurchasecustomlink/externalpurchasetype/outofapp(destinationurl:).md)
  The external purchase happens outside of the app.
- [ExternalPurchaseCustomLink.ExternalPurchaseType.withinApp](externalpurchasecustomlink/externalpurchasetype/withinapp.md)
  The external purchase happens inside the app.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static func showNotice(for: ExternalPurchaseCustomLink.ExternalPurchaseType) async throws -> ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/shownotice(for:).md)
  Displays the system disclosure notice sheet for a custom link type and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/externalpurchasetype)*