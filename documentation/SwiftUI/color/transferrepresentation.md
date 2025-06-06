# transferRepresentation

**Framework**: SwiftUI  
**Kind**: property

One group of colors–constant colors–created with explicitly specified component values are transferred as is.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var transferRepresentation: some TransferRepresentation { get }
```

#### Discussion

Another group of colors–standard colors, like `Color.mint`, and semantic colors, like `Color.accentColor`–are rendered on screen differently depending on the current [`Environment`](environment.md). For transferring, they are resolved against the default environment and might produce a slightly different result at the destination if the source of drag or copy uses a non-default environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/transferrepresentation)*