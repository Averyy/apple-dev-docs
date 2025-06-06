# registerClass(_:)

**Framework**: Quartz  
**Kind**: method

Registers a `QCPlugIn` subclass.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func registerClass(_ aClass: AnyClass!)
```

#### Discussion

You call this method only if the code for your custom patch is mixed with your application code, and you plan only to use the custom patch from within  your application.

## Parameters

- `aClass`: The   subclass.

## See Also

- [class func load(atPath: String!) -> Bool](qcplugin/load(atpath:).md)
  Loads a Quartz Composer plug-in bundle from the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/registerclass(_:))*