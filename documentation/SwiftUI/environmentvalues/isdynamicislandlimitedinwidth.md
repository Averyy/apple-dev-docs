# isDynamicIslandLimitedInWidth

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Dynamic Island appears with reduced width.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var isDynamicIslandLimitedInWidth: Bool { get }
```

#### Discussion

In some devices and context, the system adapts the flexible width of compact and minimal Live Activities and renders them smaller; for example, on iPhone in landscape orientation or on iPhone Duo. Use the `isDynamicIslandLimitedInWidth` environment value to adapt views you provide to compact and minimal Live Activity presentations. The following example shows a view for a compact leading presentation:

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isdynamicislandlimitedinwidth)*