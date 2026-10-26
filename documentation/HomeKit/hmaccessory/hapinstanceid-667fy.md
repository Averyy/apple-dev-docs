# HAPInstanceID

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- tvOS 26.1+
- visionOS 26.0+
- watchOS 26.1+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * HAPInstanceID;
```

#### Discussion

Returns the HAP Accessory Instance ID, or nil if the receiver does not represent a HAP accessory.

Requires vendor-level access to this accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/hapinstanceid-667fy)*