# isScrollEnabled

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

The default value is `true`. Use the [`scrollDisabled(_:)`](../view/scrolldisabled%28_%29.md) modifier to configure this property.

## See Also

### Disabling scrolling
- [func scrollDisabled(Bool) -> some View](../view/scrolldisabled%28_%29.md)
  Disables or enables scrolling in scrollable views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isscrollenabled)*