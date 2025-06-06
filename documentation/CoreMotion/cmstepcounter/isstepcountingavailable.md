# isStepCountingAvailable()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean indicating whether step-counting support is available on the current device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func isStepCountingAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if step-counting support is available or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

Step-counting support is not available on all iOS devices. Use this method to determine if support is available on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter/isstepcountingavailable())*