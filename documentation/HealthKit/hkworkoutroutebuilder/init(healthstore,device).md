# init(healthStore:device:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new workout route builder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(healthStore: HKHealthStore, device: HKDevice?)
```

```objc
- (instancetype) initWithHealthStore:(HKHealthStore *) healthStore device:(HKDevice *) device;
```

#### Return Value

A newly initialized workout route builder.

##### Discussion

Use of this initializer is discouraged. Use [`seriesBuilder(for:)`](../hkworkoutbuilder/seriesbuilder%28for%29.md) instead.

## Parameters

- `healthStore`: The HealthKit store.
- `device`: An object representing the device that provided the location data. Pass `nil` if the app is generating its own location data (for example, using [Core Location](../../CoreLocation/CoreLocation.md)).

## See Also

### Creating the builder
- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](../hkworkoutbuilder/seriesbuilder%28for%29.md)
  Returns the series builder for the specified type, creating a new builder, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/init(healthstore:device:))*