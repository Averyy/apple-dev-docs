# systemAction

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The handler asks the system to open the original URL.

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
static let systemAction: OpenURLAction.Result
```

#### Discussion

The action invokes its completion handler with a value that depends on the outcome of the system’s attempt to open the URL.

## See Also

### Getting the results
- [static let discarded: OpenURLAction.Result](./discarded.md)
  The handler discarded the URL.
- [static let handled: OpenURLAction.Result](./handled.md)
  The handler opened the URL.
- [static func systemAction(URL) -> OpenURLAction.Result](./systemaction%28_%29.md)
  The handler asks the system to open the modified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openurlaction/result/systemaction)*