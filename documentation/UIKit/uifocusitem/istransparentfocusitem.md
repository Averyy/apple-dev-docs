# isTransparentFocusItem

**Framework**: UIKit  
**Kind**: property

Indicates if the focus item is transparent, which allows items behind it to become focused.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var isTransparentFocusItem: Bool { get }
```

#### Discussion

The system ignores this value when the item is focusable, in which case the item is never considered transparent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/istransparentfocusitem)*