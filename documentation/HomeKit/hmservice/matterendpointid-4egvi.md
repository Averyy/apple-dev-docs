# matterEndpointID

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * matterEndpointID;
```

## Discussion

The Matter endpoint identifier that this service is mapped to.

This property is nil for HAP accessories, and set to a valid value for Matter devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/matterendpointid-4egvi)*