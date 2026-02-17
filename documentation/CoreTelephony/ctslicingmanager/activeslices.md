# activeSlices

**Framework**: Core Telephony  
**Kind**: property

Information about currently active network slices on the device.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
final var activeSlices: [CTSlicingManager.Slice] { get async throws }
```

#### Return Value

An array of [`CTSlicingManager.Slice`](ctslicingmanager/slice.md) structures, each containing `appCategory`, `trafficClass`, and `networkInterfaceName`.

#### Discussion

This property returns an array of [`CTSlicingManager.Slice`](ctslicingmanager/slice.md) structures containing detailed information about each active network slice, including the app category, traffic class, and network interface name.

Use this property to monitor which network slices currently run, and to validate that your preferred slice activates successfully.

```swift
do {
    let slices = try await CTSlicingManager.shared.activeSlices

    for slice in slices {
        print("Active slice:")
        print("  Category: \(slice.appCategory.description)")
        print("  Traffic Class: \(slice.trafficClass.description)")
        print("  Interface: \(slice.networkInterfaceName)")
    }
} catch POSIXError.ENOTSUP {
    print("Network slicing isn't currently available.")
} catch {
    print("Error retrieving active slices: \(error)")
}
```

> **Note**: - `POSIXError.ENOTSUP` if network slicing is not currently available.
- `POSIXError.EINVAL` if an invalid parameter or system error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/activeslices)*