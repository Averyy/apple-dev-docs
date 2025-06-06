# callAsFunction()

**Framework**: SwiftUI  
**Kind**: method

Initiates a refresh action.

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
func callAsFunction() async
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`RefreshAction`](refreshaction.md) structure that you get from the [`Environment`](environment.md):

```swift
struct RefreshableView: View {
    @Environment(\.refresh) private var refresh

    var body: some View {
        Button("Refresh") {
            Task {
                await refresh?()  // Implicitly calls refresh.callAsFunction()
            }
        }
        .disabled(refresh == nil)
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in . For information about asynchronous operations in Swift, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/refreshaction/callasfunction())*