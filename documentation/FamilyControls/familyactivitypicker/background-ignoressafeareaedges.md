# background(_:ignoresSafeAreaEdges:)

**Framework**: FamilyControls  
**Kind**: method

Sets the view’s background to a style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background<S>(_ style: S, ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View where S : ShapeStyle
```

#### Return Value

A view with the specified style drawn behind it.

#### Discussion

Use this modifier to place a type that conforms to the `ShapeStyle` protocol — like a `Color`, `Material`, or `HierarchicalShapeStyle` — behind a view. For example, you can add the `ShapeStyle/regularMaterial` behind a `Label`:

```swift
struct FlagLabel: View {
    var body: some View {
        Label("Flag", systemImage: "flag.fill")
            .padding()
            .background(.regularMaterial)
    }
}
```

SwiftUI anchors the style to the view’s bounds. For the example above, the background fills the entirety of the label’s frame, which includes the padding:

SwiftUI limits the background style’s extent to the modified view’s container-relative shape. You can see this effect if you constrain the `FlagLabel` view with a `View/containerShape(_:)` modifier:

```swift
FlagLabel()
    .containerShape(RoundedRectangle(cornerRadius: 16))
```

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can provide a specific set of edges to ignore, or an empty set to respect safe area insets on all edges:

```swift
Rectangle()
    .background(
        .regularMaterial,
        ignoresSafeAreaEdges: []) // Ignore no safe area insets.
```

If you want to specify a `View` or a stack of views as the background, use `View/background(alignment:content:)` instead. To specify a `Shape` or `InsettableShape`, use `View/background(_:in:fillStyle:)` . To configure the background of a presentation, like a sheet, use `View/presentationBackground(_:)`.

## Parameters

- `style`: An instance of a type that conforms to   that   SwiftUI draws behind the modified view.
- `edges`: The set of edges for which to ignore safe area insets   when adding the background. The default value is  .   Specify an empty set to respect safe area insets on all edges.

## See Also

- [func border<S>(S, width: CGFloat) -> some View](familyactivitypicker/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-180sg.md)
  Sets the view’s background to a shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-3jkgw.md)
  Sets the view’s background to a shape filled with a style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-7fmje.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-2cobx.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func listRowBackground<V>(V?) -> some View](familyactivitypicker/listrowbackground(_:).md)
  Places a custom background view behind a list row item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/background(_:ignoressafeareaedges:))*