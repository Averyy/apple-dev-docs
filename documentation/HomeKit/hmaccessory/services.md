# services

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of services provided by the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var services: [HMService] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMService *> * services;
```

## See Also

### Controlling accessory features
- [class HMService](../hmservice.md)
  A controllable feature of an accessory, like a light attached to a garage door opener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/services)*