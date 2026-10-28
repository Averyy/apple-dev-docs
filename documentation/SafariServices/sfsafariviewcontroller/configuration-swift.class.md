# SFSafariViewController.Configuration

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface SFSafariViewControllerConfiguration : NSObject
```

## Overview

Use a configuration object with the [`init(url:configuration:)`](./init%28url,configuration%29-305vl.md) method to initialize your view controller.

## Topics

### Configuring a Safari View Controller
- [var entersReaderIfAvailable: Bool](./configuration-swift.class/entersreaderifavailable.md)
  A value that specifies whether Safari should enter Reader mode, if it is available.
- [var barCollapsingEnabled: Bool](./configuration-swift.class/barcollapsingenabled.md)
- [var eventAttribution: UIEventAttribution?](./configuration-swift.class/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.
### Instance Properties
- [var activityButton: SFSafariViewController.ActivityButton?](./configuration-swift.class/activitybutton.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a View Controller
- [init(url: URL, configuration: SFSafariViewController.Configuration)](./init%28url,configuration%29-305vl.md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [convenience init(url: URL)](./init%28url%29-5kpkn.md)
  Initializes a Safari view controller that loads the specified URL.
- [init(url: URL, entersReaderIfAvailable: Bool)](./init%28url,entersreaderifavailable%29-3aatz.md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.class)*