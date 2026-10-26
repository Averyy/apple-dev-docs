# CMIOExtensionStreamCustomClockConfiguration

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that describes the parameters to create a custom clock on the host side.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStreamCustomClockConfiguration
```

```objc
@interface CMIOExtensionStreamCustomClockConfiguration : NSObject
```

## Topics

### Creating a Clock Configuration
- [init(clockName: String, sourceIdentifier: UUID, getTimeCallMinimumInterval: CMTime, numberOfEventsForRateSmoothing: UInt32, numberOfAveragesForRateSmoothing: UInt32)](./cmioextensionstreamcustomclockconfiguration/init%28clockname,sourceidentifier,gettimecallminimuminterval,numberofeventsforratesmoothing,numberofaveragesforratesmoothing%29.md)
  Creates a custom clock configuration.
- [+ customClockConfigurationWithClockName:sourceIdentifier:getTimeCallMinimumInterval:numberOfEventsForRateSmoothing:numberOfAveragesForRateSmoothing:](./cmioextensionstreamcustomclockconfiguration/customclockconfigurationwithclockname_sourceidentifier_gettimecallminimuminterval_numberofeventsforratesmoothing_numberofaveragesforratesmoothing_.md)
  Returns a new a custom clock configuration.
### Inspecting the Configuration
- [var clockName: String](./cmioextensionstreamcustomclockconfiguration/clockname.md)
  The name of the clock.
- [var sourceIdentifier: UUID](./cmioextensionstreamcustomclockconfiguration/sourceidentifier.md)
  A universally unique identifier for the clock.
- [var getTimeCallMinimumInterval: CMTime](./cmioextensionstreamcustomclockconfiguration/gettimecallminimuminterval.md)
  A minimum call time interval for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](./cmioextensionstreamcustomclockconfiguration/numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.
- [var numberOfAveragesForRateSmoothing: UInt32](./cmioextensionstreamcustomclockconfiguration/numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.
### Initializers
- [init?(coder: NSCoder)](./cmioextensionstreamcustomclockconfiguration/init%28coder%29.md)

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
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Inspecting a Stream
- [var source: (any CMIOExtensionStreamSource)?](./cmioextensionstream/source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](./cmioextensionstream/direction-swift.property.md)
  The data-flow direction of the stream.
- [CMIOExtensionStream.Direction](./cmioextensionstream/direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](./cmioextensionstream/clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](./cmioextensionstream/clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](./cmioextensionstream/customclockconfiguration.md)
  An optional custom clock configuration for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration)*