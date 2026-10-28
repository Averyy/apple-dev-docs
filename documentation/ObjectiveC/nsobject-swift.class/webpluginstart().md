# webPlugInStart()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Tells the plug-in to start normal operation.

**Availability**:
- macOS

## Declaration

```swift
func webPlugInStart()
```

```objc
- (void) webPlugInStart;
```

## Discussion

The plug-in usually begins its primary task (such as drawing, playing sounds, or animating) in this method. This method may be called more than once, provided that the application has already called [`webPlugInInitialize()`](./webplugininitialize%28%29.md) and that each call to this method is followed later by a call to [`webPlugInStop()`](./webpluginstop%28%29.md).

## See Also

### Controlling the Plug-in
- [func webPlugInDestroy()](./webplugindestroy%28%29.md)
  Prepares the plug-in for deallocation.
- [func webPlugInInitialize()](./webplugininitialize%28%29.md)
  Initializes the plug-in.
- [func webPlugInStop()](./webpluginstop%28%29.md)
  Tells the plug-in to stop normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstart())*