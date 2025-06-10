# pin

**Framework**: CryptoTokenKit  
**Kind**: property

The PIN value resulting from performing the operation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var pin: String? { get set }
```

#### Discussion

This property is set to the result of the operation after `finishWithError:` is called.

> **Note**:  If the [`apduTemplate`](tktokensmartcardpinauthoperation/apdutemplate.md) property has a set value, this property is not set, as the PIN is automatically sent to the Smart Card using the specified template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/pin)*