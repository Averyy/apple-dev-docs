# init(healthStore:device:)

**Framework**: HealthKit  
**Kind**: init

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

#### Return Value

A newly initialized workout route builder.

## Parameters

- `healthStore`: The HealthKit store.
- `device`: An object representing the device that provided the location data. Pass   if the app is generating its own location data (for example, using  ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/init(healthstore:device:))*