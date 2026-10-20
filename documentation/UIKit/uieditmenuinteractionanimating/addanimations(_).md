# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds a closure that performs animations to run alongside the edit menu interaction presentation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func addAnimations(_ animations: @escaping () -> Void)
```

```objc
- (void) addAnimations:(void (^)()) animations;
```

## Parameters

- `animations`: A closure that performs animations.

## See Also

### Adding Animations
- [func addCompletion(() -> Void)](./addcompletion%28_%29.md)
  Adds a closure to perform operations when the edit menu interaction presentation animations are complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating/addanimations(_:))*