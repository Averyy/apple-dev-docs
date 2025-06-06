# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a navigation split view.

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
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

SwiftUI calls this method for each instance of [`NavigationSplitView`](navigationsplitview.md), where this style is the current [`NavigationSplitViewStyle`](navigationsplitviewstyle.md).

## Parameters

- `configuration`: The properties of the instance to create.

## See Also

- [NavigationSplitViewStyle.Configuration](navigationsplitviewstyle/configuration.md)
  The properties of a navigation split view instance.
- [associatedtype Body : View](navigationsplitviewstyle/body.md)
  A view that represents the body of a navigation split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitviewstyle/makebody(configuration:))*