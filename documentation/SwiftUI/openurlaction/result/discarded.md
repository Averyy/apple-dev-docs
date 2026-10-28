# discarded

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The handler discarded the URL.

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
static let discarded: OpenURLAction.Result
```

## Discussion

The action invokes its completion handler with `false` when your handler returns this value.

## See Also

### Getting the results
- [static let handled: OpenURLAction.Result](./handled.md)
  The handler opened the URL.
- [static let systemAction: OpenURLAction.Result](./systemaction.md)
  The handler asks the system to open the original URL.
- [static func systemAction(URL) -> OpenURLAction.Result](./systemaction%28_%29.md)
  The handler asks the system to open the modified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/result/discarded)*