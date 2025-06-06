# interruptedPurchasesEnabled

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that determines whether the test environment simulates an interrupted purchase.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var interruptedPurchasesEnabled: Bool { get set }
```

#### Discussion

The default value is `false`. Enabling this property causes all purchases to fail until you disable it.

During testing, resolve the interrupted purchase by calling [`resolveIssueForTransaction(identifier:)`](sktestsession/resolveissuefortransaction(identifier:).md) for the affected transaction.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](sktestsession/resettodefaultstate().md) to revert all settings to those in the configuration file.

## See Also

- [func resolveIssueForTransaction(identifier: Int) throws](sktestsession/resolveissuefortransaction(identifier:).md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/interruptedpurchasesenabled)*