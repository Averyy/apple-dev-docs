# makeSharedContext()

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Create shared context to apply to previews. The context returned here will be cached and passed into the `body` method for every preview that applies a modifier of this type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
static func makeSharedContext() async throws -> Self.Context
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewmodifier/makesharedcontext())*