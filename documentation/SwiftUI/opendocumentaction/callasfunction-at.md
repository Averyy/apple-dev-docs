# callAsFunction(at:)

**Framework**: SwiftUI  
**Kind**: method

Opens the document at the specified file URL.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func callAsFunction(at url: URL) async throws
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`openDocument`](environmentvalues/opendocument.md) action:

```swift
do {
    try await openDocument(at: url)
} catch {
    // Handle error
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `url`: A file URL that points at an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/opendocumentaction/callasfunction(at:))*