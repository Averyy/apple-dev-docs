# updateChartDescriptor(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Update the existing `AXChartDescriptor` for your view, based on changes in your view or in the `Environment`.

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
func updateChartDescriptor(_ descriptor: AXChartDescriptor)
```

#### Discussion

This will be called as needed, when accessibility needs your `AXChartDescriptor` for VoiceOver. It will only be called if the inputs to your views, or a relevant part of the `Environment`, have changed.

## See Also

- [func makeChartDescriptor() -> AXChartDescriptor](axchartdescriptorrepresentable/makechartdescriptor.md)
  Create the `AXChartDescriptor` for this view, and return it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/axchartdescriptorrepresentable/updatechartdescriptor(_:))*