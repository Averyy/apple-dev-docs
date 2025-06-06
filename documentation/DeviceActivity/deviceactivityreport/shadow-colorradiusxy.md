# shadow(color:radius:x:y:)

**Framework**: DeviceActivity  
**Kind**: method

Adds a shadow to this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some View
```

#### Return Value

A view that adds a shadow to this view.

#### Discussion

Use this modifier to add a shadow of a specified color behind a view. You can offset the shadow from its view independently in the horizontal and vertical dimensions using the `x` and `y` parameters. You can also blur the edges of the shadow using the `radius` parameter. Use a radius of zero to create a sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each box displays its radius and offset values for reference.

```swift
struct Shadow: View {
    let steps = [0, 5, 10]

    var body: some View {
        VStack(spacing: 50) {
            ForEach(steps, id: \.self) { offset in
                HStack(spacing: 50) {
                    ForEach(steps, id: \.self) { radius in
                        Color.blue
                            .shadow(
                                color: .primary,
                                radius: CGFloat(radius),
                                x: CGFloat(offset), y: CGFloat(offset))
                            .overlay {
                                VStack {
                                    Text("\(radius)")
                                    Text("(\(offset), \(offset))")
                                }
                            }
                    }
                }
            }
        }
    }
}
```

The example above uses `Color/primary` as the color to make the shadow easy to see for the purpose of illustration. In practice, you might prefer something more subtle, like `Color/gray-8j2b`. If you don’t specify a color, the method uses a semi-transparent black.

## Parameters

- `color`: The shadow’s color.
- `radius`: A measure of how much to blur the shadow. Larger values   result in more blur.
- `x`: An amount to offset the shadow horizontally from the view.
- `y`: An amount to offset the shadow vertically from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/shadow(color:radius:x:y:))*