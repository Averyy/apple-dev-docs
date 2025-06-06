# thresholdAmount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The balance an account reaches before you apply the automatic reload amount.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var thresholdAmount: NSDecimalNumber { get set }
```

#### Discussion

You automatically apply the reload amount to the account when the account balance drops below the threshold amount.

Use the [`amount`](pkpaymentsummaryitem/amount.md) property to specify the reload amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentsummaryitem/thresholdamount)*