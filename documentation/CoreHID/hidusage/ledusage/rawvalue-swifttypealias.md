# HIDUsage.LEDUsage.RawValue

**Framework**: Core HID  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- macOS 15.0+

## Declaration

```swift
typealias RawValue = UInt16
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/ledusage/rawvalue-swift.typealias)*