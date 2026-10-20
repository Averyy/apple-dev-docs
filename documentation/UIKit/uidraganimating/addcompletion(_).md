# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an animation completion block to run when a view animation has ended.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

```objc
- (void) addCompletion:(void (^)(UIViewAnimatingPosition finalPosition)) completion;
```

## Parameters

- `completion`: A block that sets animatable view properties.

## See Also

### Adding animations
- [func addAnimations(() -> Void)](./addanimations%28_%29.md)
  Adds an animation block for modifying a view animation while it’s running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraganimating/addcompletion(_:))*