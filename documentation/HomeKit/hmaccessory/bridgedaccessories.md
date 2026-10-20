# bridgedAccessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var bridgedAccessories: [HMAccessory] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMAccessory *> * bridgedAccessories;
```

#### Discussion

If the receiver represents a bridge, an array of the accessories behind the bridge, otherwise empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/bridgedaccessories)*