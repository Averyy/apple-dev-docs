# loadNonExecutablePlugIn(_:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Loads a non-executable plug-in specified by its URL.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func loadNonExecutablePlugIn(_ url: URL!)
```

```objc
+ (void) loadNonExecutablePlugIn:(NSURL *) url;
```

## Discussion

If the filters contain executable code the plugin isn’t loaded.

## Parameters

- `url`: The location of the plugin to load.

## See Also

### Loading Plug-ins
- [class func loadNonExecutablePlugIns()](./loadnonexecutableplugins%28%29.md)
  Scans directories for plugins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/loadnonexecutableplugin(_:))*