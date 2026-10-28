# loadNonExecutablePlugIns()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Scans directories for plugins.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func loadNonExecutablePlugIns()
```

```objc
+ (void) loadNonExecutablePlugIns;
```

## Discussion

This call scans for plugins with the extension `.plugin` in the following directories:

- /Library/Graphics/Image Units
- ~Library/Graphics/Image Units

This call adds new plug-ins. It doesn’t remove any plug-ins.

## See Also

### Loading Plug-ins
- [class func loadNonExecutablePlugIn(URL!)](./loadnonexecutableplugin%28_%29.md)
  Loads a non-executable plug-in specified by its URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/loadnonexecutableplugins())*