# invalidate()

**Framework**: CallKit  
**Kind**: method

Invalidates the provider and completes all active calls with an error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

After a receiver is invalidated, no additional messages are sent to its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/invalidate())*