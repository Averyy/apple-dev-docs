# OpenURLAction.Result

**Framework**: SwiftUI  
**Kind**: struct

The result of a custom open URL action.

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
struct Result
```

#### Overview

If you declare a custom [`OpenURLAction`](openurlaction.md) in the [`Environment`](environment.md), return one of the result values from its handler.

- Use [`handled`](openurlaction/result/handled.md) to indicate that the handler opened the URL.
- Use [`discarded`](openurlaction/result/discarded.md) to indicate that the handler discarded the URL.
- Use [`systemAction`](openurlaction/result/systemaction.md) without an argument to ask SwiftUI to open the URL with the system handler.
- Use [`systemAction(_:)`](openurlaction/result/systemaction(_:).md) with a URL argument to ask SwiftUI to open the specified URL with the system handler.

You can use the last option to transform URLs, while still relying on the system to open the URL. For example, you could append a path component to every URL:

```swift
.environment(\.openURL, OpenURLAction { url in
    .systemAction(url.appendingPathComponent("edit"))
})
```

## Topics

### Getting the results
- [static let discarded: OpenURLAction.Result](openurlaction/result/discarded.md)
  The handler discarded the URL.
- [static let handled: OpenURLAction.Result](openurlaction/result/handled.md)
  The handler opened the URL.
- [static let systemAction: OpenURLAction.Result](openurlaction/result/systemaction.md)
  The handler asks the system to open the original URL.
- [static func systemAction(URL) -> OpenURLAction.Result](openurlaction/result/systemaction(_:).md)
  The handler asks the system to open the modified URL.
### Type Methods
- [static func systemAction(URL?, prefersInApp: Bool) -> OpenURLAction.Result](openurlaction/result/systemaction(_:prefersinapp:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(handler: (URL) -> OpenURLAction.Result)](openurlaction/init(handler:).md)
  Creates an action that opens a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/result)*