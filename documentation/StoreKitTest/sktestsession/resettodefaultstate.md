# resetToDefaultState()

**Framework**: StoreKit Test  
**Kind**: method

Removes all property overrides and resets all test session settings to their default state.

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
func resetToDefaultState()
```

#### Discussion

During testing, your tests may override the property settings such as the [`timeRate`](sktestsession/timerate-swift.property.md), [`askToBuyEnabled`](sktestsession/asktobuyenabled.md), [`interruptedPurchasesEnabled`](sktestsession/interruptedpurchasesenabled.md), and [`billingGracePeriodIsEnabled`](sktestsession/billinggraceperiodisenabled.md). Call this method to revert all the property settings to the states defined in the StoreKit configuration file that you use to initialize this [`SKTestSession`](sktestsession.md) instance.

See [`clearTransactions()`](sktestsession/cleartransactions().md) to remove all transactions from the testing environment.

## See Also

- [convenience init(configurationFileNamed: String) throws](sktestsession/init(configurationfilenamed:).md)
  Initializes the test session with the provided configuration file that you include in your application’s bundle.
- [init(contentsOf: URL) throws](sktestsession/init(contentsof:).md)
  Initializes the test session with a configuration file you provide through a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/resettodefaultstate())*