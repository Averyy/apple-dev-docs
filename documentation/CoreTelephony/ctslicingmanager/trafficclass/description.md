# description

**Framework**: Core Telephony  
**Kind**: property

A string representation of the traffic class.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
var description: String { get }
```

#### Discussion

This property provides a string representation of the traffic class, suitable for debugging and logging purposes.

> ❗ **Important**: This description isn’t localized, so don’t display it to people in your app’s interface. For text that people see, provide your own localized strings based on the traffic class value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/trafficclass/description)*