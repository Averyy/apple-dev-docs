# ExternalPurchaseCustomLink.ExternalPurchaseType

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values that represent the types of external purchase an app can perform.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
enum ExternalPurchaseType
```

## Topics

### External purchase types
- [ExternalPurchaseCustomLink.ExternalPurchaseType.outOfApp(destinationURL:)](./externalpurchasetype/outofapp%28destinationurl%29.md)
  The external purchase happens outside of the app.
- [ExternalPurchaseCustomLink.ExternalPurchaseType.withinApp](./externalpurchasetype/withinapp.md)
  The external purchase happens inside the app.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying the disclosure sheet
- [static func showNotice(for: ExternalPurchaseCustomLink.ExternalPurchaseType) async throws -> ExternalPurchaseCustomLink.NoticeResult](./shownotice%28for%29.md)
  Displays the system disclosure notice sheet for a custom link type and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeResult](./noticeresult.md)
  The result of showing the disclosure notice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/externalpurchasetype)*