# blur(radius:opaque:)

**Framework**: FinanceKitUI  
**Kind**: method

Applies a Gaussian blur to this view.

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
func blur(radius: CGFloat, opaque: Bool = false) -> some View
```

#### Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of this view.

The example below shows two `Text` views, the first with no blur effects, the second with `blur(radius:opaque:)` applied with the `radius` set to `2`. The larger the radius, the more diffuse the effect.

```None
struct Blur: View {
    var body: some View {
        VStack {
            Text("This is some text.")
                .padding()
            Text("This is some blurry text.")
                .blur(radius: 2.0)
        }
    }
}
```

## Parameters

- `radius`: The radial size of the blur. A blur is more diffuse when its   radius is large.
- `opaque`: A Boolean value that indicates whether the blur renderer   permits transparency in the blur output. Set to   to create an   opaque blur, or set to   to permit transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/blur(radius:opaque:))*