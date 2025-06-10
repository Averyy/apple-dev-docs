# fontDesign(_:)

**Framework**: App Intents  
**Kind**: method

Sets the font design of the text in this view.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS ?+
- watchOS 9.1+

## Declaration

```swift
nonisolated
func fontDesign(_ design: Font.Design?) -> some View
```

#### Return Value

A view that uses the font design you specify.

## Parameters

- `design`: One of the available font designs.   Providing   removes the effect of any font design   modifier applied higher in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/fontdesign(_:))*