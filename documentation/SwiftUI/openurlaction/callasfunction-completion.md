# callAsFunction(_:completion:)

**Framework**: SwiftUI  
**Kind**: method

Asynchronously opens a URL, following system conventions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction(_ url: URL, completion: @escaping (Bool) -> Void)
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`OpenURLAction`](openurlaction.md) structure that you get from the [`Environment`](environment.md), using a URL and a completion handler as arguments:

```swift
struct OpenURLExample: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Button {
            if let url = URL(string: "https://www.example.com") {
                // Implicitly calls openURL.callAsFunction(url) { ... }
                openURL(url) { accepted in
                    print(accepted ? "Success" : "Failure")
                }
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
- `completion`: A closure the method calls after determining if   it can open the URL, but possibly before fully opening the URL.   The closure takes a Boolean value that indicates whether the   method can open the URL.

## See Also

- [func callAsFunction(URL)](openurlaction/callasfunction(_:).md)
  Opens a URL, following system conventions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/callasfunction(_:completion:))*