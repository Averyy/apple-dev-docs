# current

**Framework**: UIKit  
**Kind**: property

An object that represents the current device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var current: UIDevice { get }
```

#### Return Value

A singleton object that represents the current device.

#### Discussion

You access the properties of the returned [`UIDevice`](uidevice.md) instance to obtain information about the device. You must instantiate the [`UIDevice`](uidevice.md) instance before registering to receive device notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/current)*