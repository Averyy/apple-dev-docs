# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the specified completion block to the animator.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
func addCompletion(_ completion: @escaping (Bool) -> Void)
```

```objc
- (void) addCompletion:(void (^)(BOOL finished)) completion;
```

## See Also

### Managing animations
- [func addAnimations(() -> Void)](./addanimations%28_%29.md)
  Adds the specified animation block to the animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractionanimating/addcompletion(_:))*