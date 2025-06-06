# delegate

**Framework**: ARKit  
**Kind**: property

An object you supply that implements coaching event callbacks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@IBOutlet
@MainActor weak var delegate: (any ARCoachingOverlayViewDelegate)? { get set }
```

#### Discussion

Normally, you set the value of this property to your app’s view controller.

## See Also

- [protocol ARCoachingOverlayViewDelegate](arcoachingoverlayviewdelegate.md)
  A set of callbacks you implement to be notified of coaching events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/delegate)*