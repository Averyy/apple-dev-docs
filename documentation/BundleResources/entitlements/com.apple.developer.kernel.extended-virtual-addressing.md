# Extended Virtual Addressing Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may access an extended address space.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+

## Details

- **Name**: `com.apple.developer.kernel.extended-virtual-addressing` (Extended Virtual Addressing)
- **Type**: boolean

## Discussion

Use this entitlement if your app has specific needs that require a larger addressable space. For example, games that memory map assets to stream to the GPU may benefit from a larger address space.

Enable this entitlement with the “Extended Virtual Addressing” capability in the Xcode project editor.

## See Also

### Memory
- [com.apple.developer.kernel.increased-memory-limit](./com.apple.developer.kernel.increased-memory-limit.md)
  A Boolean value that indicates whether core features of your app may perform better with a higher memory limit on supported devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.kernel.extended-virtual-addressing)*