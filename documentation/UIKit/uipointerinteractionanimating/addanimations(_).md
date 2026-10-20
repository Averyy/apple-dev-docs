# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the specified animation block to the animator.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
func addAnimations(_ animations: @escaping () -> Void)
```

```objc
- (void) addAnimations:(void (^)()) animations;
```

## See Also

### Managing animations
- [func addCompletion((Bool) -> Void)](./addcompletion%28_%29.md)
  Adds the specified completion block to the animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractionanimating/addanimations(_:))*