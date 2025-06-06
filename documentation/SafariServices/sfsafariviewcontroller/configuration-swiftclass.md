# SFSafariViewController.Configuration

**Framework**: Safari Services  
**Kind**: class

A configuration object that defines how a Safari view controller should be initialized.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class Configuration
```

#### Overview

Use a configuration object with the [`init(url:configuration:)`](sfsafariviewcontroller/init(url:configuration:).md) method to initialize your view controller.

## Topics

### Configuring a Safari View Controller
- [var entersReaderIfAvailable: Bool](sfsafariviewcontroller/configuration-swift.class/entersreaderifavailable.md)
  A value that specifies whether Safari should enter Reader mode, if it is available.
- [var barCollapsingEnabled: Bool](sfsafariviewcontroller/configuration-swift.class/barcollapsingenabled.md)
- [var eventAttribution: UIEventAttribution?](sfsafariviewcontroller/configuration-swift.class/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.
### Instance Properties
- [var activityButton: SFSafariViewController.ActivityButton?](sfsafariviewcontroller/configuration-swift.class/activitybutton.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(url: URL, configuration: SFSafariViewController.Configuration)](sfsafariviewcontroller/init(url:configuration:).md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [convenience init(url: URL)](sfsafariviewcontroller/init(url:).md)
  Initializes a Safari view controller that loads the specified URL.
- [init(url: URL, entersReaderIfAvailable: Bool)](sfsafariviewcontroller/init(url:entersreaderifavailable:).md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class)*