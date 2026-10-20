# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A view that represents the appearance and interaction of a toggle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
associatedtype Body : View
```

#### Discussion

SwiftUI infers this type automatically based on the [`View`](../view.md) instance that you return from your implementation of the [`makeBody(configuration:)`](./makebody%28configuration%29.md) method.

## See Also

### Creating custom toggle styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](./makebody%28configuration%29.md)
  Creates a view that represents the body of a toggle.
- [struct ToggleStyleConfiguration](../togglestyleconfiguration.md)
  The properties of a toggle instance.
- [ToggleStyle.Configuration](./configuration.md)
  The properties of a toggle instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/body)*