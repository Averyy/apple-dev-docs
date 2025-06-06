# animationTimeInterval

**Framework**: Screen Saver  
**Kind**: property

The time interval between animation frames.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var animationTimeInterval: TimeInterval { get set }
```

#### Discussion

If your screen saver has particular requirements for time between animation frames, call this method to set the animation rate to a reasonable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/animationtimeinterval)*