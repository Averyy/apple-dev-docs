# CIPlugInRegistration

**Framework**: Core Image  
**Kind**: protocol  
**Role**: Protocol

The interface for loading Core Image image units.

**Availability**:
- macOS

## Declaration

```swift
protocol CIPlugInRegistration
```

```objc
@protocol CIPlugInRegistration
```

## Overview

The principal class of an image unit—a loadable bundle containing custom Core Image filters for macOS—must support this protocol.

## Topics

### Initializing Plug-ins
- [func load(UnsafeMutableRawPointer!) -> Bool](./cipluginregistration/load%28_%29.md)
  Loads and initializes an image unit, performing custom tasks as needed.

## See Also

### Image Units
- [class CIPlugIn](./ciplugin.md)
  The mechanism for loading image units in macOS.
- [class CIFilterGenerator](./cifiltergenerator.md)
  An object that creates and configures chains of individual image filters.
- [protocol CIFilterConstructor](./cifilterconstructor.md)
  A general interface for objects that produce filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipluginregistration)*