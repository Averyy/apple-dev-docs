# activatesAutomatically

**Framework**: ARKit  
**Kind**: property

A flag that indicates whether the coaching view activates automatically, depending on the current session state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var activatesAutomatically: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true). If enabled, the coaching overlay sets [`isActive`](arcoachingoverlayview/isactive.md) automatically, depending on whether it needs user intervention to meet the current [`goal`](arcoachingoverlayview/goal-swift.property.md). The coaching overlay activates when the session is initializing or when tracking conditions have degraded past a certain threshold.

## See Also

- [var isActive: Bool](arcoachingoverlayview/isactive.md)
  A flag that indicates whether coaching is in progress.
- [func setActive(Bool, animated: Bool)](arcoachingoverlayview/setactive(_:animated:).md)
  Controls whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/activatesautomatically)*