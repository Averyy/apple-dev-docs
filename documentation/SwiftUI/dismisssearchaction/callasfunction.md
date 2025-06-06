# callAsFunction()

**Framework**: SwiftUI  
**Kind**: method

Dismisses the current search operation, if any.

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
@MainActor
@preconcurrency func callAsFunction()
```

#### Discussion

Don’t call this method directly. SwiftUI calls it for you when you call the [`DismissSearchAction`](dismisssearchaction.md) structure that you get from the [`Environment`](environment.md):

```swift
struct SearchedView: View {
    @Environment(\.dismissSearch) private var dismissSearch

    var body: some View {
        Button("Cancel") {
            dismissSearch() // Implicitly calls dismissSearch.callAsFunction()
        }
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismisssearchaction/callasfunction())*