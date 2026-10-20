# OpenURLAction.Result

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

If you declare a custom [`OpenURLAction`](../openurlaction.md) in the [`Environment`](../environment.md), return one of the result values from its handler.

- Use [`handled`](./result/handled.md) to indicate that the handler opened the URL.
- Use [`discarded`](./result/discarded.md) to indicate that the handler discarded the URL.
- Use [`systemAction`](./result/systemaction.md) without an argument to ask SwiftUI to open the URL with the system handler.
- Use [`systemAction(_:)`](./result/systemaction%28_%29.md) with a URL argument to ask SwiftUI to open the specified URL with the system handler.

You can use the last option to transform URLs, while still relying on the system to open the URL. For example, you could append a path component to every URL:

```swift
.environment(\.openURL, OpenURLAction { url in
    .systemAction(url.appendingPathComponent("edit"))
})
```

## Topics

### Getting the results
- [static let discarded: OpenURLAction.Result](./result/discarded.md)
  The handler discarded the URL.
- [static let handled: OpenURLAction.Result](./result/handled.md)
  The handler opened the URL.
- [static let systemAction: OpenURLAction.Result](./result/systemaction.md)
  The handler asks the system to open the original URL.
- [static func systemAction(URL) -> OpenURLAction.Result](./result/systemaction%28_%29.md)
  The handler asks the system to open the modified URL.
### Type Methods
- [static func systemAction(URL?, prefersInApp: Bool) -> OpenURLAction.Result](./result/systemaction%28_,prefersinapp%29.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating the action
- [init(handler: (URL) -> OpenURLAction.Result)](./init%28handler%29.md)
  Creates an action that opens a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/result)*