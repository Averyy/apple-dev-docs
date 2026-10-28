# registerClass(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Registers a `QCPlugIn` subclass.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func registerClass(_ aClass: AnyClass!)
```

```objc
+ (void) registerPlugInClass:(Class) aClass;
```

## Discussion

You call this method only if the code for your custom patch is mixed with your application code, and you plan only to use the custom patch from within  your application.

## Parameters

- `aClass`: The `QCPlugIn` subclass.

## See Also

### Loading Bundle and Custom Patches Manually
- [class func load(atPath: String!) -> Bool](./load%28atpath%29.md)
  Loads a Quartz Composer plug-in bundle from the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/registerclass(_:))*