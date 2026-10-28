# dropOffLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s destination.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var dropOffLocation: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

## Discussion

Use this property with the [`pickupLocation`](./pickuplocation.md) property to determine availability, pricing, and timing information for your rides.

## See Also

### Getting the Pickup and Drop Off Locations
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The user’s starting location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintent/dropofflocation)*