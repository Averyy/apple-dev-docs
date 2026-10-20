# childBehaviors

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the array of dynamic behaviors that are children of a custom dynamic behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var childBehaviors: [UIDynamicBehavior] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof UIDynamicBehavior *> * childBehaviors;
```

#### Discussion

Only custom subclasses of the class can have child behaviors.

## See Also

### Configuring a dynamic behavior
- [var action: (() -> Void)?](./action.md)
  The block you want to execute during dynamic animation.
- [func addChildBehavior(UIDynamicBehavior)](./addchildbehavior%28_%29.md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [func removeChildBehavior(UIDynamicBehavior)](./removechildbehavior%28_%29.md)
  Removes a child dynamic behavior from a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/childbehaviors)*