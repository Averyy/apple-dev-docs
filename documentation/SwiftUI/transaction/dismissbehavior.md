# dismissBehavior

**Framework**: SwiftUI  
**Kind**: property

The behavior for how windows will dismiss programmatically when used in conjunction with [`DismissWindowAction`](dismisswindowaction.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dismissBehavior: DismissBehavior { get set }
```

#### Discussion

The default value is `.interactive`.

You can use this property to dismiss windows which may be showing a modal presentation by using the `.destructive` value:

```swift
struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            withTransaction(\.dismissBehavior, .destructive) {
                dismissWindow(id: "auxiliary")
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction/dismissbehavior)*