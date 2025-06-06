# visible

**Framework**: SwiftUI  
**Kind**: property

Show the scroll indicators.

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
static var visible: ScrollIndicatorVisibility { get }
```

#### Discussion

The actual visibility of the indicators depends on platform conventions like auto-hiding behaviors in iOS or user preference behaviors in macOS.

## See Also

- [static var automatic: ScrollIndicatorVisibility](scrollindicatorvisibility/automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var hidden: ScrollIndicatorVisibility](scrollindicatorvisibility/hidden.md)
  Hide the scroll indicators.
- [static var never: ScrollIndicatorVisibility](scrollindicatorvisibility/never.md)
  Scroll indicators should never be visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/visible)*