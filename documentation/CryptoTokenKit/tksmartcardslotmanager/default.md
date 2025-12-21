# default

**Framework**: CryptoTokenKit  
**Kind**: property

The shared singleton Smart Card reader slot manager.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class var `default`: TKSmartCardSlotManager? { get }
```

#### Discussion

This method returns `nil` unless the [`com.apple.security.smartcard`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.smartcard) entitlement is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/default)*