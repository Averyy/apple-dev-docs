# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of view representing the body of this view.

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

When you create a custom view, Swift infers this type from your implementation of the required [`body`](./body-8kl5o.md) property.

## See Also

### Implementing a custom view
- [var body: Self.Body](./body-8kl5o.md)
  The content and behavior of the view.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](./modifier%28_%29.md)
  Applies a modifier to a view and returns a new view.
- [Previews in Xcode](../previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/body-swift.associatedtype)*