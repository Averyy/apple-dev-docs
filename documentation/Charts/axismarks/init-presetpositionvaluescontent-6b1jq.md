# init(preset:position:values:content:)

**Framework**: Swift Charts  
**Kind**: init

Creates axis markers with the given properties,will override default markers.

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
nonisolated
init(preset: AxisMarkPreset = .automatic, position: AxisMarkPosition = .automatic, values: AxisMarkValues = .automatic, @AxisMarkBuilder content: @escaping () -> Content)
```

## Parameters

- `preset`: The preset of the axis markers.
- `position`: The position of the axis markers.
- `values`: The values of the axis markers.
- `content`: A result builder that returns the content of the axis marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarks/init(preset:position:values:content:)-6b1jq)*