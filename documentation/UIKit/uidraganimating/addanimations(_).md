# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an animation block for modifying a view animation while it’s running.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addAnimations(_ animations: @escaping () -> Void)
```

```objc
- (void) addAnimations:(void (^)()) animations;
```

## Parameters

- `animations`: A block that sets animatable view properties.

## See Also

### Adding animations
- [func addCompletion((UIViewAnimatingPosition) -> Void)](./addcompletion%28_%29.md)
  Adds an animation completion block to run when a view animation has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraganimating/addanimations(_:))*