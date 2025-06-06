# backingStoreType()

**Framework**: Screen Saver  
**Kind**: method

Returns the type of backing store you want for your screen saver’s window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class func backingStoreType() -> NSWindow.BackingStoreType
```

#### Discussion

This method returns [`NSWindow.BackingStoreType.buffered`](https://developer.apple.com/documentation/AppKit/NSWindow/BackingStoreType/buffered) by default. If you want to change the backing store type, override this method and return a new value. If you override the method, you don’t need to call the inherited version.

## See Also

- [class func performGammaFade() -> Bool](screensaverview/performgammafade.md)
  Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/backingstoretype())*