# default

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, readonly, nullable) TKSmartCardSlotManager * defaultManager;
```

## Discussion

This method returns `nil` unless the [`com.apple.security.smartcard`](../../BundleResources/entitlements/com.apple.security.smartcard.md) entitlement is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/default)*