# isDynamicIslandLimitedInWidth

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Dynamic Island appears with reduced width.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
var isDynamicIslandLimitedInWidth: Bool { get }
```

## Discussion

Sometimes the system renders compact and minimal Live Activities with a limited width, for example, on iPhone in landscape orientation, on iPhone Duo, or on iPhone 18 Pro with two or more active Live Activities. Use the `isDynamicIslandLimitedInWidth` environment value to adapt your views to the reduced width of the Dynamic Island as shown in the following example:

```swift
struct CompactLeadingView: View {
    @Environment(\.isDynamicIslandLimitedInWidth) var isDynamicIslandLimitedInWidth

    var body: some View {
        if isDynamicIslandLimitedInWidth {
            Text("Ltd")
        } else {
            Text("Full")
        }
    }
}
```

To avoid truncated text, adapt your compact presentation to the limited width; for example by using a short abbreviation or graphic representation instead of a full text string. If you can’t find a solution to display views for leading and trailing compact presentations with limited width, provide a compact leading presentation that best represents your Live Activity, such as the view you use for the minimal presentation, and an empty view for the trailing compact presentation. The system hides the empty trailing view automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isdynamicislandlimitedinwidth)*