# performGammaFade()

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Type Method

Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func performGammaFade() -> Bool
```

```objc
+ (BOOL) performGammaFade;
```

#### Discussion

This class method allows the screen saver view to select how the desktop visibly transitions to the screen saver view. When this method returns [`true`](../../Swift/true.md), the screen gradually darkens before the animation begins. When it returns [`false`](../../Swift/false.md), the screen transitions immediately to the screen saver. The latter behavior is more appropriate if the screen saver animates a screenshot of the desktop, as is the case for optical lens effects. The default is [`true`](../../Swift/true.md).

## See Also

### Getting the preferred window behavior
- [class func backingStoreType() -> NSWindow.BackingStoreType](./backingstoretype%28%29.md)
  Returns the type of backing store you want for your screen saver’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/performgammafade())*