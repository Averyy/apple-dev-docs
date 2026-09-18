# ExternalPurchaseCustomLink.ExternalPurchaseType.outOfApp(destinationURL:)

**Framework**: StoreKit  
**Kind**: case

The external purchase happens outside of the app.

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
case outOfApp(destinationURL: URL?)
```

#### Discussion

> **Note**: This API requires the `destinationURL` parameter in all regions except the EU; omitting it in other regions throws an error.

## See Also

- [ExternalPurchaseCustomLink.ExternalPurchaseType.withinApp](externalpurchasecustomlink/externalpurchasetype/withinapp.md)
  The external purchase happens inside the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/externalpurchasetype/outofapp(destinationurl:))*