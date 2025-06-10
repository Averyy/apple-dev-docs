# value(_:_:unit:calendar:)

**Framework**: Swift Charts  
**Kind**: method

Creates a parameter value with label and value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func value(_ labelResource: LocalizedStringResource, _ date: Date, unit: Calendar.Component, calendar: Calendar? = nil) -> PlottableValue<Value> where Value == Date
```

## Parameters

- `labelResource`: The localized string resource for label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/plottablevalue/value(_:_:unit:calendar:)-1rtpi)*