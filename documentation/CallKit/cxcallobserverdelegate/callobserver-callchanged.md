# callObserver(_:callChanged:)

**Framework**: CallKit  
**Kind**: method  
**Required**: Yes

Called when a call is changed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func callObserver(_ callObserver: CXCallObserver, callChanged call: CXCall)
```

## Parameters

- `callObserver`: The call observer for the delegate.
- `call`: The call that has been changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate/callobserver(_:callchanged:))*