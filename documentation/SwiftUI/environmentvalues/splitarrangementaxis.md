# splitArrangementAxis

**Framework**: SwiftUI  
**Kind**: property

The axis of the split for a view within a split arrangement view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var splitArrangementAxis: Axis? { get set }
```

#### Discussion

Use this value to read the axis that a split arrangement is using to place its views. Views can adapt their layout or appearance based on whether the split is horizontal or vertical. The value is `nil` when the view is not contained within a split arrangement view.

```swift
struct DetailsView: View {
    @Environment(\.splitArrangementAxis) var axis

    var body: some View {
        let layout: AnyLayout = axis == .horizontal
            ? AnyLayout(VStackLayout())
            : AnyLayout(HStackLayout())
        layout {
            Artwork()
            Metadata()
        }
    }
}
```

## See Also

- [var overlayArrangementZIndex: Int](environmentvalues/overlayarrangementzindex.md)
  The z-index for a view within an overlay arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/splitarrangementaxis)*