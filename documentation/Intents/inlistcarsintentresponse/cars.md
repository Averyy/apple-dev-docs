# cars

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var cars: [INCar]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INCar *> * cars;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INCar *> * cars;
```

## Discussion

Set this property to an array of [`INCar`](../incar.md) objects that represents the user’s electric vehicles. Maps requires these vehicles to respond to [`INGetCarPowerLevelStatusIntent`](../ingetcarpowerlevelstatusintent.md) requests so that it can use them during route planning and navigation.

## See Also

### Providing a List of Cars
- [class INCar](../incar.md)
  A specific electric vehicle that Maps uses during route planning and navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponse/cars)*