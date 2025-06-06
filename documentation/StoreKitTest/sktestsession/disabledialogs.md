# disableDialogs

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that determines whether the testing environment disables dialogs during automated testing.

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
var disableDialogs: Bool { get set }
```

#### Discussion

The default value is `false`. Set this value to `true` when you run automated tests and want to suppress interactive dialogs.

## See Also

- [var storefront: String](sktestsession/storefront.md)
  The three-letter code that represents the region associated with the App Store storefront.
- [var locale: Locale](sktestsession/locale.md)
  The value that determines the localization metadata the test environment uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/disabledialogs)*