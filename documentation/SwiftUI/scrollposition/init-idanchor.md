# init(id:anchor:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new scroll position to a view with a provided identity value.

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
init(id: some Hashable & Sendable, anchor: UnitPoint? = nil)
```

#### Discussion

The type of the ID indicates the type of ID of views within a scroll target layout the scroll view should look for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/init(id:anchor:))*