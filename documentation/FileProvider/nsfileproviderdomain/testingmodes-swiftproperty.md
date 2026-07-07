# testingModes

**Framework**: File Provider  
**Kind**: property

A mode that gives the File Provider extension more control over the system’s behavior during testing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var testingModes: NSFileProviderDomain.TestingModes { get set }
```

#### Discussion

By default, the value is `[]` (Swift) or `0` (Objective-C) and all testing modes are disabled. To enable a testing mode, assign its value to this property. You can combine multiple modes:

```swift
myDomain.testingModes = [.alwaysEnabled, .interactive]
```

> ❗ **Important**:  You must add the [`com.apple.developer.fileprovider.testing-mode`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode) entitlement to your target before assigning a non-empty value to this property. You can only use this entitlement during testing and development. If you add it to your app or extension, you must remove it before you submit your app to TestFlight or the Mac App Store.

The system registers the domain’s testing mode when you add the domain by calling [`add(_:completionHandler:)`](nsfileprovidermanager/add(_:completionhandler:).md). You can’t change the test mode after you add the domain.

## See Also

- [NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.struct.md)
  Modes that modify the system’s behavior while testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/testingmodes-swift.property)*