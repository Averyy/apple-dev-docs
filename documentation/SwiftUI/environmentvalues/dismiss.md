# dismiss

**Framework**: SwiftUI  
**Kind**: property

An action that dismisses the current presentation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var dismiss: DismissAction { get }
```

## Mentions

- [Managing search interface activation](managing-search-interface-activation.md)

#### Discussion

Use this environment value to get the [`DismissAction`](dismissaction.md) instance for the current [`Environment`](environment.md). Then call the instance to perform the dismissal. You call the instance directly because it defines a [`callAsFunction()`](dismissaction/callasfunction().md) method that Swift calls when you call the instance.

You can use this action to:

- Dismiss a modal presentation, like a sheet or a popover.
- Pop the current view from a [`NavigationStack`](navigationstack.md).

On apps targetting iOS 18 and aligned releases, you also use the dismiss action to pop the implicit stack of a collapsed [`NavigationSplitView`](navigationsplitview.md), or clear the equivalent state in an expanded split view.

The specific behavior of the action depends on where you call it from. For example, you can create a button that calls the [`DismissAction`](dismissaction.md) inside a view that acts as a sheet:

```swift
private struct SheetContents: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Button("Done") {
            dismiss()
        }
    }
}
```

When you present the `SheetContents` view, someone can dismiss the sheet by tapping or clicking the sheet’s button:

```swift
private struct DetailView: View {
    @State private var isSheetPresented = false

    var body: some View {
        Button("Show Sheet") {
            isSheetPresented = true
        }
        .sheet(isPresented: $isSheetPresented) {
            SheetContents()
        }
    }
}
```

Be sure that you define the action in the appropriate environment. For example, don’t reorganize the `DetailView` in the example above so that it creates the `dismiss` property and calls it from the [`sheet(item:onDismiss:content:)`](view/sheet(item:ondismiss:content:).md) view modifier’s `content` closure:

```swift
private struct DetailView: View {
    @State private var isSheetPresented = false
    @Environment(\.dismiss) private var dismiss // Applies to DetailView.

    var body: some View {
        Button("Show Sheet") {
            isSheetPresented = true
        }
        .sheet(isPresented: $isSheetPresented) {
            Button("Done") {
                dismiss() // Fails to dismiss the sheet.
            }
        }
    }
}
```

If you do this, the sheet fails to dismiss because the action applies to the environment where you declared it, which is that of the detail view, rather than the sheet. In fact, in macOS and iPadOS, if the `DetailView` is the root view of a window, the dismiss action closes the window instead.

The dismiss action has no effect on a view that isn’t currently presented. If you need to query whether SwiftUI is currently presenting a view, read the [`isPresented`](environmentvalues/ispresented.md) environment value.

> **Note**: While the dismiss action can be used to a close window that you create with [`WindowGroup`](windowgroup.md) or [`Window`](window.md), prefer [`DismissWindowAction`](dismisswindowaction.md) for that use case instead.

## See Also

- [var isPresented: Bool](environmentvalues/ispresented.md)
  A Boolean value that indicates whether the view associated with this environment is currently presented.
- [struct DismissAction](dismissaction.md)
  An action that dismisses a presentation.
- [func interactiveDismissDisabled(Bool) -> some View](view/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/dismiss)*