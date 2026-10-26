# AUCustomViewPersistentData

**Framework**: CoreAudioKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods an Audio Unit host calls to manage view data.

**Availability**:
- macOS 10.6+

## Declaration

```swift
protocol AUCustomViewPersistentData
```

```objc
@protocol AUCustomViewPersistentData
```

## Topics

### Accessing View State
- [var customViewPersistentData: NSDictionary?](./aucustomviewpersistentdata/customviewpersistentdata.md)
  Called by the host application to obtain view state data from a custom Cocoa view.

## Relationships

### Conforming Types
- [AUGenericView](./augenericview.md)

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
- [AUViewControllerBase](./auviewcontrollerbase.md)
  A type definition that indicates the the platform’s Audio Unit view controller base class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata)*