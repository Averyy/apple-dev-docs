# grayscale(_:)

**Framework**: App Intents  
**Kind**: method

Adds a grayscale effect to this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func grayscale(_ amount: Double) -> some View
```

#### Return Value

A view that adds a grayscale effect to this view.

#### Discussion

A grayscale effect reduces the intensity of colors in this view.

The example below shows a series of red squares with their grayscale effect increasing from 0 (reddest) to 99% (fully desaturated) in approximate 20% increments:

```swift
struct Saturation: View {
    var body: some View {
        HStack {
            ForEach(0..<6) {
                Color.red.frame(width: 60, height: 60, alignment: .center)
                    .grayscale(Double($0) * 0.1999)
                    .overlay(Text("\(Double($0) * 0.1999 * 100, specifier: "%.4f")%"),
                             alignment: .bottom)
                    .border(Color.gray)
            }
        }
    }
}
```

## Parameters

- `amount`: The intensity of grayscale to apply from 0.0 to less   than 1.0. Values closer to 0.0 are more colorful, and values closer to   1.0 are less colorful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/grayscale(_:))*