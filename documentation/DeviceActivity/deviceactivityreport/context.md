# DeviceActivityReport.Context

**Framework**: DeviceActivity  
**Kind**: struct

A context indicating how your device activity report extension should configure its `DeviceActivityReportView`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Context
```

#### Overview

You can use a [`DeviceActivityReport.Context`](deviceactivityreport/context.md) to create a [`DeviceActivityReport`](deviceactivityreport.md), which the system then provides to your app’s extension and allows it to configure the resulting report `View` in a particular way. For example, if you want to render either a pie chart or bar graph representing the user’s device activity, you can create the following custom contexts:

```swift
extension DeviceActivityReport.Context {
    static let barGraph = Self("barGraph")
    static let pieChart = Self("pieChart")
}
```

If your app instantiates a report with the `barGraph` context, then the system prompts your report extension to generate a view using the `Scene` corresponding to that context.

## Topics

### Initializers
- [init(String)](deviceactivityreport/context/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: String)](deviceactivityreport/context/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](deviceactivityreport/context/rawvalue-swift.property.md)
  The underlying value that represents the given context.
### Type Aliases
- [DeviceActivityReport.Context.RawValue](deviceactivityreport/context/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](deviceactivityreport/context/equatable-implementations.md)
- [RawRepresentable Implementations](deviceactivityreport/context/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/context)*