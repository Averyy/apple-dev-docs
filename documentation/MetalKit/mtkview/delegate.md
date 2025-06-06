# delegate

**Framework**: MetalKit  
**Kind**: property

The view’s delegate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any MTKViewDelegate)? { get set }
```

#### Discussion

A delegate is optional. If you provide one, the view calls the delegate when it needs to update its contents. You should either provide a delegate or subclass the view to override the [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) method, but not both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/delegate)*