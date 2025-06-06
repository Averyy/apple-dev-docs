# sceneBridgingOptions

**Framework**: SwiftUI  
**Kind**: property

The options for which aspects of the window will be managed by this controller’s hosting view.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }
```

#### Discussion

`NSHostingController` will populate certain aspects of its associated window, depending on which options are specified.

For example, a hosting controller can manage its window’s toolbar by including the `.toolbars` option:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                MyToolbarContent()
            }
    }
}

let controller = NSHostingController(rootView: RootView())
controller.sceneBridgingOptions = [.toolbars]
```

When this hosting controller is set as the `contentViewController` for a window, the default value for this property will be `.all`, which includes the options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.

## See Also

- [func sizeThatFits(in: CGSize) -> CGSize](nshostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var preferredContentSize: NSSize](nshostingcontroller/preferredcontentsize.md)
- [var sizingOptions: NSHostingSizingOptions](nshostingcontroller/sizingoptions.md)
  The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [var safeAreaRegions: SafeAreaRegions](nshostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/scenebridgingoptions)*