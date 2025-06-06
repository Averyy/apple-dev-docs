# viewID(type:)

**Framework**: SwiftUI  
**Kind**: method

The id of the view positioned in the scroll view if configured to be in that position or the user has scrolled past a view with an id of matching type.

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
func viewID<T>(type: T.Type) -> T? where T : Hashable, T : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/viewid(type:))*