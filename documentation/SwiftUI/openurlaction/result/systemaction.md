# systemAction(_:)

**Framework**: SwiftUI  
**Kind**: method

The handler asks the system to open the modified URL.

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
static func systemAction(_ url: URL) -> OpenURLAction.Result
```

#### Discussion

The action invokes its completion handler with a value that depends on the outcome of the system’s attempt to open the URL.

## Parameters

- `url`: The URL that the handler asks the system to open.

## See Also

- [static let discarded: OpenURLAction.Result](openurlaction/result/discarded.md)
  The handler discarded the URL.
- [static let handled: OpenURLAction.Result](openurlaction/result/handled.md)
  The handler opened the URL.
- [static let systemAction: OpenURLAction.Result](openurlaction/result/systemaction.md)
  The handler asks the system to open the original URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/result/systemaction(_:))*