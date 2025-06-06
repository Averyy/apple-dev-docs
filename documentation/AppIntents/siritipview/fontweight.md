# fontWeight(_:)

**Framework**: App Intents  
**Kind**: method

Sets the font weight of the text in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func fontWeight(_ weight: Font.Weight?) -> some View
```

#### Return Value

A view that uses the font weight you specify.

## Parameters

- `weight`: One of the available font weights.   Providing   removes the effect of any font weight   modifier applied higher in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/fontweight(_:))*