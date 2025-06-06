# webPlugInInitialize()

**Framework**: Objective-C Runtime  
**Kind**: method

Initializes the plug-in.

**Availability**:
- macOS ?+

## Declaration

```swift
func webPlugInInitialize()
```

#### Discussion

Tells the plug-in to perform one-time initialization. This method must be called only once per instance of the plug-in object, before any other methods in the protocol are called.

## See Also

- [func webPlugInDestroy()](nsobject-swift.class/webplugindestroy.md)
  Prepares the plug-in for deallocation.
- [func webPlugInStart()](nsobject-swift.class/webpluginstart.md)
  Tells the plug-in to start normal operation.
- [func webPlugInStop()](nsobject-swift.class/webpluginstop.md)
  Tells the plug-in to stop normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugininitialize())*