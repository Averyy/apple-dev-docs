# isScrollEnabled

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.

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
var isScrollEnabled: Bool { get set }
```

#### Discussion

The default value is `true`. Use the [`scrollDisabled(_:)`](view/scrolldisabled(_:).md) modifier to configure this property.

## See Also

- [func scrollDisabled(Bool) -> some View](view/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isscrollenabled)*