# default

**Framework**: CryptoTokenKit  
**Kind**: property

The shared singleton Smart Card reader slot manager.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class var `default`: TKSmartCardSlotManager? { get }
```

#### Discussion

This method returns `nil` unless the [`com.apple.security.smartcard`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.smartcard) entitlement is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/default)*