# webPlugInInitialize()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Initializes the plug-in.

**Availability**:
- macOS

## Declaration

```swift
func webPlugInInitialize()
```

```objc
- (void) webPlugInInitialize;
```

#### Discussion

Tells the plug-in to perform one-time initialization. This method must be called only once per instance of the plug-in object, before any other methods in the protocol are called.

## See Also

### Controlling the Plug-in
- [func webPlugInDestroy()](./webplugindestroy%28%29.md)
  Prepares the plug-in for deallocation.
- [func webPlugInStart()](./webpluginstart%28%29.md)
  Tells the plug-in to start normal operation.
- [func webPlugInStop()](./webpluginstop%28%29.md)
  Tells the plug-in to stop normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugininitialize())*