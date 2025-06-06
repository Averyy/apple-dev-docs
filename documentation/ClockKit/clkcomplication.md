# CLKComplication

**Framework**: ClockKit  
**Kind**: class

Metadata about a custom complication.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplication
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)
- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)

#### Overview

ClockKit defines each complication by its [`family`](clkcomplication/family.md) and [`identifier`](clkcomplication/identifier.md) properties. Each pair represents a unique complication that the user can select when configuring a watch face. When creating timeline entries, check both properties before creating and filling the complication’s template.

You specify the possible [`family`](clkcomplication/family.md) and [`identifier`](clkcomplication/identifier.md) combinations in your data source’s [`getComplicationDescriptors(handler:)`](clkcomplicationdatasource/getcomplicationdescriptors(handler:).md) method. Each of the [`CLKComplicationDescriptor`](clkcomplicationdescriptor.md) objects you provide defines a unique identifier and the families that it supports.

In watchOS 6 and earlier, each app can have only one complication per supported family. When your app creates complication templates, determine the complication’s type from its [`family`](clkcomplication/family.md) property only. For more information, see [`Declaring complications for your app`](declaring-complications-for-your-app.md).

You don’t create instances of this class directly. Instead, you retrieve them from the [`CLKComplicationServer`](clkcomplicationserver.md) object. Complication objects are only available when your complication is in use on the watch face.

In addition to getting information about the complication, you use complication objects to extend or replace the timeline data for one of your active complications. When calling the [`extendTimeline(for:)`](clkcomplicationserver/extendtimeline(for:).md) and [`reloadTimeline(for:)`](clkcomplicationserver/reloadtimeline(for:).md) methods of the shared [`CLKComplicationServer`](clkcomplicationserver.md) object, pass the complication object you want to update.

## Topics

### Accessing Data About the Complication
- [var family: CLKComplicationFamily](clkcomplication/family.md)
  The family to which the complication belongs.
- [var identifier: String](clkcomplication/identifier.md)
  An identifier that specifies a complication if your app supports multiple complications per family.
- [var userActivity: NSUserActivity?](clkcomplication/useractivity.md)
  An object that represents the state of the app at a moment in time.
- [var userInfo: [AnyHashable : Any]?](clkcomplication/userinfo.md)
  A dictionary of additional data associated with the complication.

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

- [class CLKComplicationServer](clkcomplicationserver.md)
  An object that manages the active complications for an app.
- [class CLKComplicationTimelineEntry](clkcomplicationtimelineentry.md)
  A container for the complication template object to display and the time to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplication)*