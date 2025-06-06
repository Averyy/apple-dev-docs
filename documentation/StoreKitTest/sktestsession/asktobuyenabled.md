# askToBuyEnabled

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that determines whether the testing environment simulates an Ask to Buy scenario.

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
var askToBuyEnabled: Bool { get set }
```

#### Discussion

The default value is `false`. Enabling this property causes all purchases to require approval until you disable it. To approve the purchase in the testing environment, call [`approveAskToBuyTransaction(identifier:)`](sktestsession/approveasktobuytransaction(identifier:).md), and to decline it, call [`declineAskToBuyTransaction(identifier:)`](sktestsession/declineasktobuytransaction(identifier:).md).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](sktestsession/resettodefaultstate().md) to revert all settings to those in the configuration file.

## See Also

- [func approveAskToBuyTransaction(identifier: Int) throws](sktestsession/approveasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by approving the transaction.
- [func declineAskToBuyTransaction(identifier: Int) throws](sktestsession/declineasktobuytransaction(identifier:).md)
  Resolves an Ask to Buy test scenario by declining the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/asktobuyenabled)*