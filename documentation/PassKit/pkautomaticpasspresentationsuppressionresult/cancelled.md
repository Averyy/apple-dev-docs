# PKAutomaticPassPresentationSuppressionResult.cancelled

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The system canceled the suppression before calling the response handler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
case cancelled
```

## See Also

- [PKAutomaticPassPresentationSuppressionResult.notSupported](pkautomaticpasspresentationsuppressionresult/notsupported.md)
  The device doesn’t support the suppression of automatic pass presentation.
- [PKAutomaticPassPresentationSuppressionResult.alreadyPresenting](pkautomaticpasspresentationsuppressionresult/alreadypresenting.md)
  The device is already presenting passes.
- [PKAutomaticPassPresentationSuppressionResult.denied](pkautomaticpasspresentationsuppressionresult/denied.md)
  The user prevented the suppression, or an internal error occurred.
- [PKAutomaticPassPresentationSuppressionResult.success](pkautomaticpasspresentationsuppressionresult/success.md)
  Suppression of automatic presentation successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/cancelled)*