# accessibilityChartDescriptor(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityChartDescriptor<R>(_ representable: R) -> some View where R : AXChartDescriptorRepresentable
```

#### Discussion

Use this method to provide information about your chart view to allow VoiceOver and other assistive technology users to perceive and interact with your chart and its data.

This may be applied to any View that represents a chart, including Image and custom-rendered chart views.

The `accessibilityChartDescriptor` modifier can be applied to -any- view representing a chart, the simplest case being just an image of a chart. The implementation details of the view aren’t important, only the fact that it represents a chart, and that the provided chart descriptor accurately describes the content of the chart.

Example usage:

First define your `AXChartDescriptorRepresentable` type.

```swift
struct MyChartDescriptorRepresentable:
AXChartDescriptorRepresentable {
    func makeChartDescriptor() -> AXChartDescriptor {
        // Build and return your `AXChartDescriptor` here.
    }

    func updateChartDescriptor(_ descriptor: AXChartDescriptor) {
        // Update your chart descriptor with any new values, or
        // don't override if your chart doesn't have changing
        // values.
    }
}
```

Then use the `accessibilityChartDescriptor` modifier to provide an instance of your `AXChartDescriptorRepresentable` type to the view representing your chart:

```swift
SomeChartView()
    .accessibilityChartDescriptor(MyChartDescriptorRepresentable())
```

## Parameters

- `chartDescriptor`: The    used to describe your chart and its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/accessibilitychartdescriptor(_:))*