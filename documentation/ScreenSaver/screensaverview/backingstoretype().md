# backingStoreType()

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Type Method

Returns the type of backing store you want for your screen saver’s window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func backingStoreType() -> NSWindow.BackingStoreType
```

```objc
+ (NSBackingStoreType) backingStoreType;
```

## Discussion

This method returns [`NSWindow.BackingStoreType.buffered`](../../AppKit/nswindow/backingstoretype/buffered.md) by default. If you want to change the backing store type, override this method and return a new value. If you override the method, you don’t need to call the inherited version.

## See Also

### Getting the preferred window behavior
- [class func performGammaFade() -> Bool](./performgammafade%28%29.md)
  Indicates whether to perform a gradual screen fade when the system starts and stops your screen saver’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/backingstoretype())*