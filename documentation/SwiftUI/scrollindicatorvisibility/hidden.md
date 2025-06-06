# hidden

**Framework**: SwiftUI  
**Kind**: property

Hide the scroll indicators.

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
static var hidden: ScrollIndicatorVisibility { get }
```

#### Discussion

By default, scroll views in macOS show indicators when a mouse is connected. Use [`never`](scrollindicatorvisibility/never.md) to indicate a stronger preference that can override this behavior.

## See Also

- [static var automatic: ScrollIndicatorVisibility](scrollindicatorvisibility/automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var never: ScrollIndicatorVisibility](scrollindicatorvisibility/never.md)
  Scroll indicators should never be visible.
- [static var visible: ScrollIndicatorVisibility](scrollindicatorvisibility/visible.md)
  Show the scroll indicators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/hidden)*