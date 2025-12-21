# close

**Framework**: SwiftUI  
**Kind**: property

A role that indicates a button that closes the current operation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let close: ButtonRole
```

#### Discussion

Unlike a cancel operation, a close operation doesn’t lose progress for a user.

The following view would display a close button in the toolbar.

```swift
struct NewContactSheet: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            NewContactEditor()
                .toolbar {
                    Button(role: .close) {
                        dismiss()
                    }
                }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrole/close)*