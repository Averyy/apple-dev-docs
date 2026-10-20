# rect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns an anchor source rect defined by `r` in the current view.

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
static func rect(_ r: CGRect) -> Anchor<Value>.Source
```

Available when `Value` is `CGRect`.

## See Also

### Getting rectangle anchor sources
- [static var bounds: Anchor<CGRect>.Source](./bounds.md)
  An anchor source rect defined as the entire bounding rect of the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anchor/source/rect(_:))*