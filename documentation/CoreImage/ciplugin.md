# CIPlugIn

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

The mechanism for loading image units in macOS.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class CIPlugIn
```

```objc
@interface CIPlugIn : NSObject
```

## Overview

An image unit is an image processing bundle that contains one or more Core Image filters. Th`e.plugin` extension indicates one or more filters packaged as an image unit.

> **Note**:  Starting in macOS 10.15, loading executable CIFilter plugins is deprecated.

## Topics

### Loading Plug-ins
- [class func loadNonExecutablePlugIns()](./ciplugin/loadnonexecutableplugins%28%29.md)
  Scans directories for plugins.
- [class func loadNonExecutablePlugIn(URL!)](./ciplugin/loadnonexecutableplugin%28_%29.md)
  Loads a non-executable plug-in specified by its URL.
### Deprecated
- [class func loadAllPlugIns()](./ciplugin/loadallplugins%28%29.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.
- [class func load(URL!, allowExecutableCode: Bool)](./ciplugin/load%28_,allowexecutablecode%29.md)
  Loads filters from an image unit that have the appropriate executable status.
- [+ loadPlugIn:allowNonExecutable:](./ciplugin/loadplugin_allownonexecutable_.md)
  Loads filters from an image unit that have the appropriate executable status.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Image Units
- [class CIFilterGenerator](./cifiltergenerator.md)
  An object that creates and configures chains of individual image filters.
- [protocol CIPlugInRegistration](./cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](./cifilterconstructor.md)
  A general interface for objects that produce filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin)*