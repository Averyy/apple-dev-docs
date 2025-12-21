# confirm

**Framework**: SwiftUI  
**Kind**: property

A role that indicates a button that confirms an operation.

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
static let confirm: ButtonRole
```

#### Discussion

The following view would display a confirm button in the toolbar.

```swift
struct NewContactSheet: View {
    var body: some View {
        NavigationStack {
            NewContactEditor()
                .toolbar {
                    Button(role: .confirm) {
                        saveChanges()
                    }
                }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrole/confirm)*