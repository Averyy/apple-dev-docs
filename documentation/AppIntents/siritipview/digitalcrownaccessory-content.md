# digitalCrownAccessory(content:)

**Framework**: App Intents  
**Kind**: method

Places an accessory View next to the Digital Crown on Apple Watch.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func digitalCrownAccessory<Content>(@ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

#### Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple Watch. Use `View/digitalCrownAccessory(_:)` to specify the visibility of your custom view.

```swift
struct ZoomingMapView: View {
    // Width of the map displayed on screen in miles
    @State private var zoomLevel: Int = 1.0

    var body: some View {
        CustomMap(width: .miles(zoomLevel))
            .focusable()
            .digitalCrownRotation(value: $zoomLevel)
            .digitalCrownAccessory {
                Text("\(zoomLevel, specifier: "%.2f")MI")
                .background {
                    RoundedRectangle(cornerRadius: 5)
                        .fill(Color.gray)
                }
            }
    }
}
```

## Parameters

- `content`: The view to be used as a Digital Crown Accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/digitalcrownaccessory(content:))*