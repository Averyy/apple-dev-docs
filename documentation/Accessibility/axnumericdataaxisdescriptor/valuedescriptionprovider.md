# valueDescriptionProvider

**Framework**: Accessibility  
**Kind**: property

A description to speak for a particular data value on the axis.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var valueDescriptionProvider: (Double) -> String { get set }
```

## Mentions

- [Representing chart data as an audio graph](representing-chart-data-as-an-audio-graph.md)

#### Discussion

Use this property to format data values into string representations that include units, dates, times, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/valuedescriptionprovider)*