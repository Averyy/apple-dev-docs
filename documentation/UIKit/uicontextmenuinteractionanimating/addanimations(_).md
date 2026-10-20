# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the specified animation block to the animator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addAnimations(_ animations: @escaping () -> Void)
```

```objc
- (void) addAnimations:(void (^)()) animations;
```

## Parameters

- `animations`: The animation block.

## See Also

### Adding Custom Animations
- [func addCompletion(() -> Void)](./addcompletion%28_%29.md)
  Adds the specified completion block to the animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractionanimating/addanimations(_:))*