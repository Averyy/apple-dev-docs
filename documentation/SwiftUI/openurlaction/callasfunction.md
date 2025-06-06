# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method

Opens a URL, following system conventions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction(_ url: URL)
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`OpenURLAction`](openurlaction.md) structure that you get from the [`Environment`](environment.md), using a URL as an argument:

```swift
struct OpenURLExample: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Button {
            if let url = URL(string: "https://www.example.com") {
                openURL(url) // Implicitly calls openURL.callAsFunction(url)
            }
        } label: {
            Label("Get Help", systemImage: "person.fill.questionmark")
        }
    }
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `url`: The URL to open.

## See Also

- [func callAsFunction(URL, completion: (Bool) -> Void)](openurlaction/callasfunction(_:completion:).md)
  Asynchronously opens a URL, following system conventions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/callasfunction(_:))*