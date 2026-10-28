# hidden

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

## Discussion

By default, scroll views in macOS show indicators when a mouse is connected. Use [`never`](./never.md) to indicate a stronger preference that can override this behavior.

## See Also

### Getting visibilties
- [static var automatic: ScrollIndicatorVisibility](./automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var never: ScrollIndicatorVisibility](./never.md)
  Scroll indicators should never be visible.
- [static var visible: ScrollIndicatorVisibility](./visible.md)
  Show the scroll indicators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/hidden)*