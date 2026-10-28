# ExternalPurchaseCustomLink.ExternalPurchaseType.outOfApp(destinationURL:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The external purchase happens outside of the app.

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
case outOfApp(destinationURL: URL?)
```

## Discussion

> **Note**: This API requires the `destinationURL` parameter in all regions except the EU; omitting it in other regions throws an error.

## See Also

### External purchase types
- [ExternalPurchaseCustomLink.ExternalPurchaseType.withinApp](./withinapp.md)
  The external purchase happens inside the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/externalpurchasetype/outofapp(destinationurl:))*