# PKAutomaticPassPresentationSuppressionResult.notSupported

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The device doesn’t support the suppression of automatic pass presentation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
case notSupported
```

```c
PKAutomaticPassPresentationSuppressionResultNotSupported
```

## See Also

### Constants
- [PKAutomaticPassPresentationSuppressionResult.alreadyPresenting](./alreadypresenting.md)
  The device is already presenting passes.
- [PKAutomaticPassPresentationSuppressionResult.denied](./denied.md)
  The user prevented the suppression, or an internal error occurred.
- [PKAutomaticPassPresentationSuppressionResult.cancelled](./cancelled.md)
  The system canceled the suppression before calling the response handler.
- [PKAutomaticPassPresentationSuppressionResult.success](./success.md)
  Suppression of automatic presentation successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/notsupported)*