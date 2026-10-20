# disableSlicing()

**Framework**: Core Telephony  
**Kind**: method

Disables network slicing for new connections.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
final func disableSlicing() async throws
```

#### Discussion

Call this method to stop using network slicing for your app. After calling this method, new network connections that your app establishes use the carrier’s default cellular internet without slice-specific routing.

> ❗ **Important**: This method only affects connections that the system creates after calling it. Existing active connections that already use a network slice continue to use that slice until the system closes them.

```swift
do {
    try await CTSlicingManager.shared.disableSlicing()
    // New connections use the default cellular internet.
    // Existing connections remain on their current slice.
} catch POSIXError.ENOTSUP {
    print("Network slicing operation isn't currently available.")
} catch {
    print("Failed to disable slicing: \(error)")
}
```

> **Note**: - `POSIXError.ENOTSUP` if network slicing is not currently available.
- `POSIXError.EINVAL` if an invalid parameter or system error occurs.

## See Also

- [func activatePreferredSliceForCategory(CTSlicingManager.AppCategory) async throws](ctslicingmanager/activatepreferredsliceforcategory(_:).md)
  Activates a preferred network slice for new connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/disableslicing())*