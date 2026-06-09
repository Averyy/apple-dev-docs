# preferredContentSize

**Framework**: Image Playground  
**Kind**: property

The preferred size for the view controller’s view.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var preferredContentSize: CGSize { get set }
```

#### Discussion

The view controller overrides this method to establish its preferred content size in visionOS. Changing the value of this property has no effect in visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/preferredcontentsize)*