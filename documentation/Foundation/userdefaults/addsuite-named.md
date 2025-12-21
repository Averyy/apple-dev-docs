# addSuite(named:)

**Framework**: Foundation  
**Kind**: method

Inserts settings for the specified domain into the search list of the current object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addSuite(named suiteName: String)
```

#### Discussion

This method inserts the domain for your custom suite of settings after the app domain and before the global domain. This arrangement causes the `UserDefaults` object to return your app-specific settings first, followed by settings from the specified suite. If you call this method multiple times, the `UserDefaults` object searches your suites in the order you added them.

This method doesn’t affect the destination for write operations. If you want to write settings to a custom suite, use the [`init(suiteName:)`](userdefaults/init(suitename:).md) initializer to construct a `UserDefaults` object specifically for that suite.

> ❗ **Important**: An app that accesses settings in a suite must also have the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups).

## Parameters

- `suiteName`: The bundle identifier for the domain you want to add. You don’t need   to specify a bundle identifier for another app. Instead, you might specify the   app group identifier you use to share data between multiple apps or between your   app and an app extension. Don’t specify your app’s bundle identifier or the     identifier in this parameter.

## See Also

- [func removeSuite(named: String)](userdefaults/removesuite(named:).md)
  Removes the specified domain from the search list of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/addsuite(named:))*