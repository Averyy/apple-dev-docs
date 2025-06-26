# listRowBackground(_:)

**Framework**: FamilyControls  
**Kind**: method

Places a custom background view behind a list row item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func listRowBackground<V>(_ view: V?) -> some View where V : View
```

#### Return Value

A list row view with `view` as its background view.

#### Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list row item.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI `ForEach` structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowBackground(_:)` modifier then places the view you supply behind each of the list row items:

```swift
struct ContentView: View {
    enum Flavor: String, CaseIterable, Identifiable {
        var id: String { self.rawValue }
        case vanilla, chocolate, strawberry
    }

    var body: some View {
        List {
            ForEach(Flavor.allCases) {
                Text($0.rawValue)
                    .listRowBackground(Ellipse()
                                        .background(Color.clear)
                                        .foregroundColor(.purple)
                                        .opacity(0.3)
                    )
            }
        }
    }
}
```

## Parameters

- `view`: The   to use as the background behind the list   row view.

## See Also

- [func border<S>(S, width: CGFloat) -> some View](familyactivitypicker/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-180sg.md)
  Sets the view’s background to a shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-3jkgw.md)
  Sets the view’s background to a shape filled with a style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-7fmje.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-2cobx.md)
  Sets the view’s background to an insettable shape filled with a style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/listrowbackground(_:))*