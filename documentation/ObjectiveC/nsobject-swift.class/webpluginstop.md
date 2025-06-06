# webPlugInStop()

**Framework**: Objective-C Runtime  
**Kind**: method

Tells the plug-in to stop normal operation.

**Availability**:
- macOS ?+

## Declaration

```swift
func webPlugInStop()
```

#### Discussion

This method may be called more than once, provided that the application has already called [`webPlugInInitialize()`](nsobject-swift.class/webplugininitialize().md) and that each call to this method is preceded by a call to [`webPlugInStart()`](nsobject-swift.class/webpluginstart().md).

## See Also

- [func webPlugInDestroy()](nsobject-swift.class/webplugindestroy.md)
  Prepares the plug-in for deallocation.
- [func webPlugInInitialize()](nsobject-swift.class/webplugininitialize.md)
  Initializes the plug-in.
- [func webPlugInStart()](nsobject-swift.class/webpluginstart.md)
  Tells the plug-in to start normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstop())*