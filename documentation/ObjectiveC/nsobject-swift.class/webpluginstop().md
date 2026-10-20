# webPlugInStop()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Tells the plug-in to stop normal operation.

**Availability**:
- macOS

## Declaration

```swift
func webPlugInStop()
```

```objc
- (void) webPlugInStop;
```

#### Discussion

This method may be called more than once, provided that the application has already called [`webPlugInInitialize()`](./webplugininitialize%28%29.md) and that each call to this method is preceded by a call to [`webPlugInStart()`](./webpluginstart%28%29.md).

## See Also

### Controlling the Plug-in
- [func webPlugInDestroy()](./webplugindestroy%28%29.md)
  Prepares the plug-in for deallocation.
- [func webPlugInInitialize()](./webplugininitialize%28%29.md)
  Initializes the plug-in.
- [func webPlugInStart()](./webpluginstart%28%29.md)
  Tells the plug-in to start normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstop())*