# value(_:_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Type Method

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
static func value<S>(_ label: S, _ value: Value) -> PlottableValue<Value> where S : StringProtocol
```

Available when `Value` conforms to `Plottable`.

## Parameters

- `label`: The label.
- `value`: The parameter’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/plottablevalue/value(_:_:)-13lvv)*