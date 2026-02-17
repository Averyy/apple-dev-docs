# availableSliceAppCategories

**Framework**: Core Telephony  
**Kind**: property

Network-slicing app categories available to your app.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
final var availableSliceAppCategories: [CTSlicingManager.AppCategory] { get async throws }
```

#### Discussion

This property returns an array of [`CTSlicingManager.AppCategory`](ctslicingmanager/appcategory.md) values that meet all of the following requirements:

- The carrier’s network supports them.
- Your app’s entitlements include them.
- The device and network currently make them available.

Query this property before attempting to activate a specific network slice category to ensure it’s available.

```swift
do {
    let categories = try await CTSlicingManager.shared.availableSliceAppCategories
    print("Available categories: \(categories)")
} catch POSIXError.ENOTSUP {
    print("Network slicing isn't currently available")
} catch {
    print("Error retrieving categories: \(error)")
}
```

> **Note**: - `POSIXError.ENOTSUP` if network slicing is not currently available.
- `POSIXError.EINVAL` if an invalid parameter or system error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/availablesliceappcategories)*