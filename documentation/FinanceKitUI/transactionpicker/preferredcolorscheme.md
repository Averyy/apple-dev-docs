# preferredColorScheme(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets the preferred color scheme for this presentation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
```

#### Return Value

A view that sets the color scheme.

#### Discussion

Use one of the values in `ColorScheme` with this modifier to set a preferred color scheme for the nearest enclosing presentation, like a popover, a sheet, or a window. The value that you set overrides the user’s Dark Mode selection for that presentation. In the example below, the `Toggle` controls an `isDarkMode` state variable, which in turn controls the color scheme of the sheet that contains the toggle:

```None
@State private var isPresented = false
@State private var isDarkMode = true

var body: some View {
    Button("Show Sheet") {
        isPresented = true
    }
    .sheet(isPresented: $isPresented) {
        List {
            Toggle("Dark Mode", isOn: $isDarkMode)
        }
        .preferredColorScheme(isDarkMode ? .dark : nil)
    }
}
```

If you apply the modifier to any of the views in the sheet — which in this case are a `List` and a `Toggle` — the value that you set propagates up through the view hierarchy to the enclosing presentation, or until another color scheme modifier higher in the hierarchy overrides it. The value you set also flows down to all child views of the enclosing presentation.

Pass `nil` to indicate that there is no preferred color scheme for this view. This is useful in cases where a preferred color scheme should only be applied conditionally. In the previous example, the sheet will prefer dark mode when `isDarkMode` is set to `true`, but otherwise defer to the color scheme as determined by the system.

Multiple views in the same view hierarchy can set a preferred color scheme. Applying this modifier overrides any existing preferred color scheme set for the view, such as by one of its subviews. If there are conflicting, non-`nil` color scheme preferences set by parallel branches of the view hierarchy, the system will prioritize the first non-`nil` preference based on the order of the views. In the example below, the preferred color scheme for the entire view will resolve to `.dark`, from the second view:

```None
VStack {
    Text("First")
        .preferredColorScheme(.light)
        .preferredColorScheme(nil) // overrides `.light`

    Text("Second")
        .preferredColorScheme(.dark)

    Text("Third")
        .preferredColorScheme(.light)
}
```

A common use for this modifier is to create side-by-side previews of the same view with light and dark appearances:

```None
struct MyView_Previews: PreviewProvider {
    static var previews: some View {
        MyView().preferredColorScheme(.light)
        MyView().preferredColorScheme(.dark)
    }
}
```

If you need to detect the color scheme that currently applies to a view, read the `EnvironmentValues/colorScheme` environment value:

```None
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

## Parameters

- `colorScheme`: The preferred color scheme for this view, or    to indicate no preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/preferredcolorscheme(_:))*