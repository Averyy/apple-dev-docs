# activatesAutomatically

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A flag that indicates whether the coaching view activates automatically, depending on the current session state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var activatesAutomatically: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL activatesAutomatically;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). If enabled, the coaching overlay sets [`isActive`](./isactive.md) automatically, depending on whether it needs user intervention to meet the current [`goal`](./goal-swift.property.md). The coaching overlay activates when the session is initializing or when tracking conditions have degraded past a certain threshold.

## See Also

### Activating the View
- [var isActive: Bool](./isactive.md)
  A flag that indicates whether coaching is in progress.
- [func setActive(Bool, animated: Bool)](./setactive%28_,animated%29.md)
  Controls whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/activatesautomatically)*