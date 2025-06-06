# presentationSizing(_:)

**Framework**: Realitykit  
**Kind**: method

Sets the sizing of the containing presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func presentationSizing(_ sizing: some PresentationSizing) -> some View
```

#### Discussion

Use this modifier to apply a `PresentationSizing` to a presentation like `View/sheet(isPresented:onDismiss:content:)`. The `sizing` parameter defines the size proposed to the content, and the presentation adopts the returned size. The default value is `automatic`.

Sizings can be modified to fix their dimensions based on the content, and optionally be sticky.

> **Note**: `PresentationSizing/fitted(horizontal:vertical:)` and `PresentationSizing/sticky(horizontal:vertical:)`.

> **Note**: If the presentation’s root container is a `NavigationSplitView`, the proposed width only applies to the `detail` column. The `sidebar` and `content` column widths use system-provided values, or those from `View/navigationSplitViewColumnWidth(_:)` or `View/navigationSplitViewColumnWidth(min:ideal:max:)` modifiers.

For example, a presentation with facts about flowers could prefer `.page` sizing because its content is primarily informational. Since the user can choose different flowers from the picker, each with different lengths of information, the size is fitted vertically to size the sheet to the textual content, and vertically sticky is specified to prevent the presentation from changing size too frequently as the user changes selection.

```None
struct ContentView: View {
    @State private var presentInfo = true

    var body: some View {
        ContentView.sheet(isPresented: $presentInfo) {
            VStack {
                Picker("Flower Species", selection: $flower) {
                    ForEach(Flower.allCases) {
                        Text($0.rawValue.uppercased()).tag($0)
                    }
                }
                Text(flower.emoji).font(.largeTitle)
                Text(flower.informationalText)
            }
            .frame(maxHeight: .infinity, alignment: .top)
            .padding()
            .presentationSizing(
                .page
                    .fitted(horizontal: false, vertical: true)
                    .sticky(horizontal: false, vertical: true))
        }
    }
}
```

## Parameters

- `sizing`: A value dictating size to propose to presentation content   and how the presentation responds to changes in content size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/presentationsizing(_:))*