# load(atPath:)

**Framework**: Quartz  
**Kind**: method

Loads a Quartz Composer plug-in bundle from the specified path.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func load(atPath path: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful.

#### Discussion

Call this method only if you need to load a plug-in bundle from a nonstandard location. Typically you don’t need to call this method because Quartz Composer automatically loads bundles that you install  in one of the following locations:

- `/Library/Graphics/Quartz Composer Plug-Ins`
- `~/Library/Graphics/Quartz Composer Plug-Ins`

This method does nothing if the bundle is already loaded. (This method does not load in all environments. Web Kit, for example, cannot load custom patches.)

The bundle can contain more than one `QCPlugIn` subclass. After the bundle is loaded, each `QCPlugIn` subclass appears as a patch in the Quartz Composer patch library.

## Parameters

- `path`: The location of the bundle.

## See Also

- [class func registerClass(AnyClass!)](qcplugin/registerclass(_:).md)
  Registers a `QCPlugIn` subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/load(atpath:))*