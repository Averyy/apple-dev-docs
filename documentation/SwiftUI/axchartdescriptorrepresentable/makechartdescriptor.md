# makeChartDescriptor()

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Create the `AXChartDescriptor` for this view, and return it.

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
func makeChartDescriptor() -> AXChartDescriptor
```

#### Discussion

This will be called once per identity of your `View`. It will not be run again unless the identity of your `View` changes. If you need to update the `AXChartDescriptor` based on changes in your `View`, or in the `Environment`, implement `updateChartDescriptor`. This method will only be called if / when accessibility needs the `AXChartDescriptor` of your view, for VoiceOver.

## See Also

- [func updateChartDescriptor(AXChartDescriptor)](axchartdescriptorrepresentable/updatechartdescriptor(_:).md)
  Update the existing `AXChartDescriptor` for your view, based on changes in your view or in the `Environment`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/axchartdescriptorrepresentable/makechartdescriptor())*