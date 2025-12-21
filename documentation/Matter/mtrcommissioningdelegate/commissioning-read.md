# commissioning(_:read:)

**Framework**: Matter  
**Kind**: method

Callback that gets called after various information (product identity, optionally endpoint structure information, optionally other attributes that were requested) has been read from the commissionee.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
optional func commissioning(_ commissioning: MTRCommissioningOperation, read info: MTRCommissioneeInfo)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:read:))*