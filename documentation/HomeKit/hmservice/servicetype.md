# serviceType

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The type of the service.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var serviceType: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * serviceType;
```

#### Discussion

The [`serviceType`](./servicetype.md) property contains a string that indicates what the service does. See [Accessory Service Types](../accessory-service-types.md) for a list of possible service types.

## See Also

### Getting the service type
- [Accessory Service Types](../accessory-service-types.md)
  The service types supported by HomeKit.
- [var localizedDescription: String](./localizeddescription.md)
  The localized description of the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/servicetype)*