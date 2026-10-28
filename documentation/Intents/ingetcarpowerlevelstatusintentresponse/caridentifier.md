# carIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var carIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * carIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * carIdentifier;
```

## Discussion

The `carIdentifier` is a unique value that your app provides, and must not be the vehicle’s VIN or equivalent identifier. For the best user experience—and to prevent orphaned or duplicate vehicles in the user’s My Vehicles collection—your app must always provide the same identifier for the same vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/caridentifier)*