# value(_:_:unit:calendar:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func value(_ label: Text, _ date: KeyPath<DataElement, DataValue>, unit: Calendar.Component, calendar: Calendar? = nil) -> PlottableProjection<DataElement, DataValue>
```

Available when `DataValue` conforms to `Plottable` and `DataValue.PrimitivePlottable` is `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/plottableprojection/value(_:_:unit:calendar:)-1oys9)*