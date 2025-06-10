# presentationSizing(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the sizing of the containing presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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

Use this modifier to apply a [`PresentationSizing`](presentationsizing.md) to a presentation like [`sheet(isPresented:onDismiss:content:)`](view/sheet(ispresented:ondismiss:content:).md). The `sizing` parameter defines the size proposed to the content, and the presentation adopts the returned size. The default value is `automatic`.

Sizings can be modified to fix their dimensions based on the content, and optionally be sticky.

> **Note**: [`fitted(horizontal:vertical:)`](presentationsizing/fitted(horizontal:vertical:).md) and [`sticky(horizontal:vertical:)`](presentationsizing/sticky(horizontal:vertical:).md).

> **Note**: If the presentation’s root container is a `NavigationSplitView`, the proposed width only applies to the `detail` column. The `sidebar` and `content` column widths use system-provided values, or those from [`navigationSplitViewColumnWidth(_:)`](view/navigationsplitviewcolumnwidth(_:).md) or [`navigationSplitViewColumnWidth(min:ideal:max:)`](view/navigationsplitviewcolumnwidth(min:ideal:max:).md) modifiers.

For example, a presentation with facts about flowers could prefer `.page` sizing because its content is primarily informational. Since the user can choose different flowers from the picker, each with different lengths of information, the size is fitted vertically to size the sheet to the textual content, and vertically sticky is specified to prevent the presentation from changing size too frequently as the user changes selection.

```swift
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

## See Also

- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](view/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [struct PresentationAdaptation](presentationadaptation.md)
  Strategies for adapting a presentation to a different size class.
- [protocol PresentationSizing](presentationsizing.md)
  A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [struct PresentationSizingRoot](presentationsizingroot.md)
  A proxy to a view provided to the presentation with a defined presentation size.
- [struct PresentationSizingContext](presentationsizingcontext.md)
  Contextual information about a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationsizing(_:))*