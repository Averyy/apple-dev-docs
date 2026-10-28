# pickupLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s starting location.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var pickupLocation: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * pickupLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * pickupLocation;
```

## Discussion

Use this property to determine what vehicles are in the vicinity. Combine this property with the [`dropOffLocation`](./dropofflocation.md) property to determine pricing and timing information.

## See Also

### Getting the Pickup and Drop Off Locations
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The user’s destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintent/pickuplocation)*