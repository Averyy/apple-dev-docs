# status()

**Framework**: ProximityReader  
**Kind**: method

Allows the merchant to check the status of the Store and Forward session.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func status() async throws -> StoreAndForwardStatus
```

#### Return Value

[`StoreAndForwardStatus`](storeandforwardstatus.md) when successful.

#### Discussion

> **Note**: This method throws a `ReadError` if status cannot be retrieved.

This method throws a `ReadError` if status cannot be retrieved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardpaymentcardreadersession/status())*