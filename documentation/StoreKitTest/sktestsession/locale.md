# locale

**Framework**: StoreKit Test  
**Kind**: property

The value that determines the localization metadata the test environment uses.

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
var locale: Locale { get set }
```

#### Discussion

This value determines the locale the test environment uses when it fetches localized metadata for [`SKProductsRequest`](https://developer.apple.com/documentation/StoreKit/SKProductsRequest). You provide localized metadata in your StoreKit configuration file.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](sktestsession/resettodefaultstate().md) to revert all settings to those in the configuration file.

## See Also

- [var storefront: String](sktestsession/storefront.md)
  The three-letter code that represents the region associated with the App Store storefront.
- [var disableDialogs: Bool](sktestsession/disabledialogs.md)
  A Boolean value that determines whether the testing environment disables dialogs during automated testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/locale)*