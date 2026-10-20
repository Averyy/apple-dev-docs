# AUAudioUnitViewConfiguration

**Framework**: CoreAudioKit  
**Kind**: class  
**Role**: Class

A configuration object that describes how to present the audio unit’s user interface.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class AUAudioUnitViewConfiguration
```

```objc
@interface AUAudioUnitViewConfiguration : NSObject
```

## Topics

### Creating a Configuration
- [init(width: CGFloat, height: CGFloat, hostHasController: Bool)](./auaudiounitviewconfiguration/init%28width,height,hosthascontroller%29.md)
  Creates a new configuration object.
### Accessing Settings
- [var width: CGFloat](./auaudiounitviewconfiguration/width.md)
  The configured width.
- [var height: CGFloat](./auaudiounitviewconfiguration/height.md)
  The configured height.
- [var hostHasController: Bool](./auaudiounitviewconfiguration/hosthascontroller.md)
  A Boolean value that indicates whether the host shows its own control surface in this view configuration.
### Initializers
- [init?(coder: NSCoder)](./auaudiounitviewconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Audio Units
- [class AUViewController](./auviewcontroller.md)
  The base class to extend when creating a custom user interface for an audio unit.
- [class AUGenericView](./augenericview.md)
  A view that provides a generic user interface for a Cocoa audio unit.
- [class AUPannerView](./aupannerview.md)
  A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- [protocol AUCustomViewPersistentData](./aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/auaudiounitviewconfiguration)*