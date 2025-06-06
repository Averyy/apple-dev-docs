# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Adds an animation completion block to run when a view animation has ended.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

## Parameters

- `completion`: A block that sets animatable view properties.

## See Also

- [func addAnimations(() -> Void)](uidraganimating/addanimations(_:).md)
  Adds an animation block for modifying a view animation while it’s running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraganimating/addcompletion(_:))*