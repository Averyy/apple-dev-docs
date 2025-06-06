# never

**Framework**: SwiftUI  
**Kind**: property

Scroll indicators should never be visible.

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
static var never: ScrollIndicatorVisibility { get }
```

#### Discussion

This value behaves like [`hidden`](scrollindicatorvisibility/hidden.md), but overrides scrollable views that choose to keep their indidicators visible. When using this value, provide an alternative method of scrolling. The typical horizontal swipe gesture might not be available, depending on the current input device.

## See Also

- [static var automatic: ScrollIndicatorVisibility](scrollindicatorvisibility/automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var hidden: ScrollIndicatorVisibility](scrollindicatorvisibility/hidden.md)
  Hide the scroll indicators.
- [static var visible: ScrollIndicatorVisibility](scrollindicatorvisibility/visible.md)
  Show the scroll indicators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/never)*