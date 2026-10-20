# never

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

This value behaves like [`hidden`](./hidden.md), but overrides scrollable views that choose to keep their indicators visible. When using this value, provide an alternative method of scrolling. The typical horizontal swipe gesture might not be available, depending on the current input device.

## See Also

### Getting visibilties
- [static var automatic: ScrollIndicatorVisibility](./automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var hidden: ScrollIndicatorVisibility](./hidden.md)
  Hide the scroll indicators.
- [static var visible: ScrollIndicatorVisibility](./visible.md)
  Show the scroll indicators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/never)*