# askToBuyEnabled

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL askToBuyEnabled;
```

#### Discussion

The default value is `false`. Enabling this property causes all purchases to require approval until you disable it. To approve the purchase in the testing environment, call [`approveAskToBuyTransaction(identifier:)`](./approveasktobuytransaction%28identifier%29.md), and to decline it, call [`declineAskToBuyTransaction(identifier:)`](./declineasktobuytransaction%28identifier%29.md).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](./resettodefaultstate%28%29.md) to revert all settings to those in the configuration file.

## See Also

### Testing Ask To Buy transactions
- [func approveAskToBuyTransaction(identifier: Int) throws](./approveasktobuytransaction%28identifier%29.md)
  Resolves an Ask to Buy test scenario by approving the transaction.
- [func declineAskToBuyTransaction(identifier: Int) throws](./declineasktobuytransaction%28identifier%29.md)
  Resolves an Ask to Buy test scenario by declining the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/asktobuyenabled)*