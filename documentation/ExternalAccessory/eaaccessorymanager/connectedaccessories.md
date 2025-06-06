# connectedAccessories

**Framework**: External Accessory  
**Kind**: property

The accessory objects corresponding to the list of currently connected accessories.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var connectedAccessories: [EAAccessory] { get }
```

#### Discussion

This property contains an array of [`EAAccessory`](eaaccessory.md) objects. Each object corresponds to an accessory that is connected and available for your application to use. Because the contents of this property can change dynamically based on the connection and disconnection of accessories, you should not cache the value of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/connectedaccessories)*