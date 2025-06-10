# resetEligibility()

**Framework**: TipKit  
**Kind**: method

Reset a previously invalidated tip.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func resetEligibility() async
```

#### Overview

By default tips that are invalidated will never become eligible for display. This prevents tips about already discovered features from appearing. Resetting a tip changes its status back to `.pending` or `.available` and makes it re-eligible for display.

```swift
struct CatTrackSettings: View {
    var body: some View {
        VStack {
            LocationSettings()
            MapSettings()

            Button("Reset Map Tips") {
                Task {
                    let reorientMapTip = ReorientMapTip()
                    await reorientMapTip.resetEligibility()

                    let compassMapTip = CompassMapTip()
                    await compassMapTip.resetEligibility()
                }
            }
        }
    }
}
```

## See Also

- [func invalidate(reason: Self.InvalidationReason)](tip/invalidate(reason:).md)
  Permanently invalidates a tip and prevents it from displaying.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/reseteligibility())*