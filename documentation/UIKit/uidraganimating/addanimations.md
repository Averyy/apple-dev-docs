# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Adds an animation block for modifying a view animation while it’s running.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAnimations(_ animations: @escaping () -> Void)
```

## Parameters

- `animations`: A block that sets animatable view properties.

## See Also

- [func addCompletion((UIViewAnimatingPosition) -> Void)](uidraganimating/addcompletion(_:).md)
  Adds an animation completion block to run when a view animation has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraganimating/addanimations(_:))*