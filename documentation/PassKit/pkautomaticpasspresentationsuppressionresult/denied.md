# PKAutomaticPassPresentationSuppressionResult.denied

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The user prevented the suppression, or an internal error occurred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
case denied
```

```c
PKAutomaticPassPresentationSuppressionResultDenied
```

## See Also

### Constants
- [PKAutomaticPassPresentationSuppressionResult.notSupported](./notsupported.md)
  The device doesn’t support the suppression of automatic pass presentation.
- [PKAutomaticPassPresentationSuppressionResult.alreadyPresenting](./alreadypresenting.md)
  The device is already presenting passes.
- [PKAutomaticPassPresentationSuppressionResult.cancelled](./cancelled.md)
  The system canceled the suppression before calling the response handler.
- [PKAutomaticPassPresentationSuppressionResult.success](./success.md)
  Suppression of automatic presentation successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/denied)*