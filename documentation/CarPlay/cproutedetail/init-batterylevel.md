# init(batteryLevel:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for battery percentage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(batteryLevel: Double)
```

#### Return Value

A new @c CPRouteDetail instance representing the battery level

#### Discussion

Use this method to display the estimated battery level upon arrival at the destination for electric vehicles. Display as a percentage (0.0 to 100.0) to show state of charge.

Percentage-based battery display is familiar to most users and provides an intuitive understanding of remaining range. The system formats this as a percentage with appropriate visual indicators. Values are clamped to the 0.0-100.0 range if necessary.

> **Note**: For more technical users or when absolute capacity is more relevant, consider using @c routeDetailWithKilowattHours: to show energy in kilowatt-hours instead.

## Parameters

- `batteryLevel`: The battery level as a percentage from 0.0 (empty) to 100.0 (full). Values outside this range will be clamped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(batterylevel:))*