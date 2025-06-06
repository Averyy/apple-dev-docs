# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addCompletion(_ completion: @escaping () -> Void)
```

## Parameters

- `completion`: A closure that performs operations after the animations complete.

## See Also

- [func addAnimations(() -> Void)](uieditmenuinteractionanimating/addanimations(_:).md)
  Adds a closure that performs animations to run alongside the edit menu interaction presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating/addcompletion(_:))*