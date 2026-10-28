# isStepCountingAvailable()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a Boolean indicating whether step-counting support is available on the current device.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CMPedometer instead

## Declaration

```swift
class func isStepCountingAvailable() -> Bool
```

```objc
+ (BOOL) isStepCountingAvailable;
```

## Return Value

[`true`](../../Swift/true.md) if step-counting support is available or [`false`](../../Swift/false.md) if it is not.

## Discussion

Step-counting support is not available on all iOS devices. Use this method to determine if support is available on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable())*