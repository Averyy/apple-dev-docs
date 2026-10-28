# fileSystemSubType

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A property for the file system’s subtype or flavor.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var fileSystemSubType: Int { get set }
```

```objc
@property NSInteger fileSystemSubType;
```

## Discussion

Match this value to the `FSPersonalities`‘s `FSSubType` attribute, if it exists within the `EXAppExtensionAttributes` dictionary of the module’s `Info.plist`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsstatfsresult/filesystemsubtype)*