# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the specified completion block to the animator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addCompletion(_ completion: @escaping () -> Void)
```

```objc
- (void) addCompletion:(void (^)()) completion;
```

## Parameters

- `completion`: The completion block.

## See Also

### Adding Custom Animations
- [func addAnimations(() -> Void)](./addanimations%28_%29.md)
  Adds the specified animation block to the animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractionanimating/addcompletion(_:))*