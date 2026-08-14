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

Use a configuration object with the [`init(url:configuration:)`](sfsafariviewcontroller/init(url:configuration:)-305vl.md) method to initialize your view controller.

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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [init(url: URL, configuration: SFSafariViewController.Configuration)](sfsafariviewcontroller/init(url:configuration:)-305vl.md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [convenience init(url: URL)](sfsafariviewcontroller/init(url:)-5kpkn.md)
  Initializes a Safari view controller that loads the specified URL.
- [init(url: URL, entersReaderIfAvailable: Bool)](sfsafariviewcontroller/init(url:entersreaderifavailable:)-3aatz.md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class)*