# AUViewControllerBase

**Framework**: CoreAudioKit  
**Kind**: typealias  
**Role**: Type Alias

A type definition that indicates the the platform’s Audio Unit view controller base class.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```c
typedef UIViewController AUViewControllerBase;
```

*macOS*

```c
typedef NSViewController AUViewControllerBase;
```

## See Also

### Audio Units
- [class AUViewController](./auviewcontroller.md)
  The base class to extend when creating a custom user interface for an audio unit.
- [class AUAudioUnitViewConfiguration](./auaudiounitviewconfiguration.md)
  A configuration object that describes how to present the audio unit’s user interface.
- [class AUGenericView](./augenericview.md)
  A view that provides a generic user interface for a Cocoa audio unit.
- [class AUPannerView](./aupannerview.md)
  A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- [protocol AUCustomViewPersistentData](./aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/auviewcontrollerbase)*