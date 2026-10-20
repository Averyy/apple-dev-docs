# authorizationStatus

**Framework**: Core Motion  
**Kind**: property  
**Role**: Type Property

A value indicating whether the app has user authorization to receive submersion data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class var authorizationStatus: CMAuthorizationStatus { get }
```

```objc
@property (class, nonatomic, readonly) CMAuthorizationStatus authorizationStatus;
```

#### Discussion

The system automatically requests authorization to access motion data the first time your app instantiates a `CMWaterSubmersionManager`. You can use this property to check the current authorization status.

## See Also

### Checking availability and authorization
- [class var waterSubmersionAvailable: Bool](./watersubmersionavailable.md)
  A Boolean value indicating whether the current device supports the submersion manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/authorizationstatus)*