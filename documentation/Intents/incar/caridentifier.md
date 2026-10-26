# carIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The electric vehicle’s unique identifier.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var carIdentifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * carIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * carIdentifier;
```

#### Discussion

The identifier is a unique value that your app provides that isn’t the vehicle’s VIN or equivalent identifier.

Use `carIdentifier` when handling [`INGetCarPowerLevelStatusIntent`](../ingetcarpowerlevelstatusintent.md) requests so that the response can match the appropriate vehicle in the user’s My Vehicles collection.

## See Also

### Identifying the Car
- [var displayName: String?](./displayname.md)
  The electric vehicle’s user-defined display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/caridentifier)*