# tipBackgroundInteraction(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls whether people can interact with the view behind a presented tip.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func tipBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
```

##### Discussion

On many platforms, SwiftUI automatically disables the view behind a popover tip that you present, so that people can’t interact with the backing view until they dismiss the tip. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind a `popoverTip`.

```swift
struct LandmarkDetail: View {
    let landmark: Landmark

    var body: some View {
        ScrollView {
            MapView(coordinate: landmark.locationCoordinate)
                .popoverTip(CampsiteTip())
                .tipBackgroundInteraction(.enabled)

            HStack {
                Text(landmark.name)
                Text(landmark.park)
            }
        }
    }
}
```

## Parameters

- `interaction`: A specification of how people can interact with the view behind a presented tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipbackgroundinteraction(_:))*