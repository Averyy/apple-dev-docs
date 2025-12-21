# performGammaFade()

**Framework**: Screen Saver  
**Kind**: method

Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class func performGammaFade() -> Bool
```

#### Discussion

This class method allows the screen saver view to select how the desktop visibly transitions to the screen saver view. When this method returns [`true`](https://developer.apple.com/documentation/Swift/true), the screen gradually darkens before the animation begins. When it returns [`false`](https://developer.apple.com/documentation/Swift/false), the screen transitions immediately to the screen saver. The latter behavior is more appropriate if the screen saver animates a screenshot of the desktop, as is the case for optical lens effects. The default is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [class func backingStoreType() -> NSWindow.BackingStoreType](screensaverview/backingstoretype.md)
  Returns the type of backing store you want for your screen saver’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/performgammafade())*