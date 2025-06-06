# controlSize(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the size for controls within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func controlSize(_ controlSize: ControlSize) -> some View
```

#### Discussion

Use `controlSize(_:)` to override the system default size for controls in this view. In this example, a view displays several typical controls at `.mini`, `.small` and `.regular` sizes.

```swift
struct ControlSize: View {
    var body: some View {
        VStack {
            MyControls(label: "Mini")
                .controlSize(.mini)
            MyControls(label: "Small")
                .controlSize(.small)
            MyControls(label: "Regular")
                .controlSize(.regular)
        }
        .padding()
        .frame(width: 450)
        .border(Color.gray)
    }
}

struct MyControls: View {
    var label: String
    @State private var value = 3.0
    @State private var selected = 1
    var body: some View {
        HStack {
            Text(label + ":")
            Picker("Selection", selection: $selected) {
                Text("option 1").tag(1)
                Text("option 2").tag(2)
                Text("option 3").tag(3)
            }
            Slider(value: $value, in: 1...10)
            Button("OK") { }
        }
    }
}
```

![A screenshot showing several controls of various](https://docs-assets.developer.apple.com/published/accf80df231061eac66e07e5377e0d31/SwiftUI-View-controlSize%402x.png)

## Parameters

- `controlSize`: One of the control sizes specified in the    enumeration.

## See Also

- [var controlSize: ControlSize](environmentvalues/controlsize.md)
  The size to apply to controls within a view.
- [enum ControlSize](controlsize.md)
  The size classes, like regular or small, that you can apply to controls within a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/controlsize(_:))*