# activatePreferredSliceForCategory(_:)

**Framework**: Core Telephony  
**Kind**: method

Activates a preferred network slice for new connections.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
final func activatePreferredSliceForCategory(_ appCategory: CTSlicingManager.AppCategory) async throws
```

#### Discussion

Call this method before establishing network connections to route your app’s traffic through a specific network slice. After calling this method, new network connections that your app establishes use the specified slice category.

The array that [`availableSliceAppCategories`](ctslicingmanager/availablesliceappcategories.md) returns must include the specified category for activation to succeed.

> ❗ **Important**: This method only affects connections that the system creates after calling it. Existing active connections continue to use their current routing until the system closes them.

```swift
do {
    // Activate the gaming slice before starting a multiplayer session.
    try await CTSlicingManager.shared.activatePreferredSliceForCategory(.gaming)

    // Establish network connections for gaming traffic.
    // New connections route through the gaming network slice.
    // Existing connections remain on their current routing.
} catch POSIXError.ENOTSUP {
    print("Network slicing isn't currently available.")
} catch {
    print("Failed to activate slice: \(error)")
}
```

> **Note**: - `POSIXError.ENOTSUP` if network slicing is not currently available.
- `POSIXError.EINVAL` if an invalid parameter or system error occurs.

## Parameters

- `appCategory`: The   to activate. Available categories include:

## See Also

- [func disableSlicing() async throws](ctslicingmanager/disableslicing.md)
  Disables network slicing for new connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/activatepreferredsliceforcategory(_:))*