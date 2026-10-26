# CLLiveUpdateConfiguration

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

Specifies the types of locations that a location updater generates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
enum CLLiveUpdateConfiguration : NSInteger;
```

## Topics

### Update types
- [CLLiveUpdateConfigurationDefault](./clliveupdateconfiguration/clliveupdateconfigurationdefault.md)
  The default configuration.
- [CLLiveUpdateConfigurationAirborne](./clliveupdateconfiguration/clliveupdateconfigurationairborne.md)
  A configuration for airborne use cases.
- [CLLiveUpdateConfigurationAutomotiveNavigation](./clliveupdateconfiguration/clliveupdateconfigurationautomotivenavigation.md)
  A configuration for automotive navigation use cases.
- [CLLiveUpdateConfigurationFitness](./clliveupdateconfiguration/clliveupdateconfigurationfitness.md)
  A configuration for fitness use cases.
- [CLLiveUpdateConfigurationOtherNavigation](./clliveupdateconfiguration/clliveupdateconfigurationothernavigation.md)
  A configuration for other navigation use cases.
### Enumeration Cases
- [CLLiveUpdateConfigurationMaritime](./clliveupdateconfiguration/clliveupdateconfigurationmaritime.md)

## See Also

### Creating a location updater
- [+ liveUpdaterWithConfiguration:queue:handler:](./cllocationupdater/liveupdaterwithconfiguration_queue_handler_.md)
  Creates a location updater with the configuration and queue that you specify.
- [+ liveUpdaterWithQueue:handler:](./cllocationupdater/liveupdaterwithqueue_handler_.md)
  Creates a location updater on the queue you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clliveupdateconfiguration)*