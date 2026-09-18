# overlayArrangementZIndex

**Framework**: SwiftUI  
**Kind**: property

The z-index for a view within an overlay arrangement view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var overlayArrangementZIndex: Int { get set }
```

#### Discussion

Use this value to read the z-ordering of a view when it is placed in an overlay arrangement. Views with a higher z-index are rendered on top of views with a lower z-index.

```swift
struct PlayerView: View {
    @Environment(\.overlayArrangementZIndex) var zIndex

    var body: some View {
        VideoPlayerControls()
            .opacity(zIndex == 0 ? 1.0 : 0.5)
    }
}
```

## See Also

- [var splitArrangementAxis: Axis?](environmentvalues/splitarrangementaxis.md)
  The axis of the split for a view within a split arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/overlayarrangementzindex)*