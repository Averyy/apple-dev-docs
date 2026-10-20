# webPlugInDestroy()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Prepares the plug-in for deallocation.

**Availability**:
- macOS

## Declaration

```swift
func webPlugInDestroy()
```

```objc
- (void) webPlugInDestroy;
```

#### Discussion

Typically, this method frees the memory and other resources used by the plug-in. For example, if the plug-in had a copy of a WebPlugInContainer object, this method should relinquish ownership of that object. Do not send any other messages to the plug-in after invoking this method, because calling this method destroys the plug-in. No other methods in this interface may be called after the application has called this method.

## See Also

### Controlling the Plug-in
- [func webPlugInInitialize()](./webplugininitialize%28%29.md)
  Initializes the plug-in.
- [func webPlugInStart()](./webpluginstart%28%29.md)
  Tells the plug-in to start normal operation.
- [func webPlugInStop()](./webpluginstop%28%29.md)
  Tells the plug-in to stop normal operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugindestroy())*