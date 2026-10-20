# CLKComplicationDataSource

**Framework**: ClockKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that provides ClockKit with information about your complication.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
protocol CLKComplicationDataSource : NSObjectProtocol
```

```objc
@protocol CLKComplicationDataSource <NSObject>
```

## Mentions

- [Enabling Complications for Your watchOS App](./enabling-complications-for-your-watchos-app.md)
- [Sharing an Apple Watch face](./sharing-an-apple-watch-face.md)

#### Overview

Apps that support a complication must define a class that supports the [`CLKComplicationDataSource`](./clkcomplicationdatasource.md) protocol and register it with the system. Your data source is responsible for providing timeline entries and data for all of the complication families that you support. You do this by implementing the protocol methods, returning the timeline entries displayed by your complication and information about the features that your complication supports.

You don’t instantiate your data source class explicitly. After defining your class, specify the class name in the General tab of the project settings for your WatchKit extension. When the system needs data, ClockKit instantiates your data source and initializes it by calling its `init` method. Once initialized, ClockKit calls the corresponding protocol methods to gather any needed data. You can also specify your class name in your app’s `Info.plist` file using the `CLKComplicationsPrincipalClass` key.

When the user installs your complication on the clock face, ClockKit creates an appropriate [`CLKComplication`](./clkcomplication.md) object for the selected complication family. ClockKit then passes the complication to your data source so that you know how to format your timeline entries. Use the General tab of your WatchKit extension’s project settings to specify the families you support.

Your complication data source class must implement the [`CLKComplicationDataSource`](./clkcomplicationdatasource.md) protocol’s [`getCurrentTimelineEntry(for:withHandler:)`](./clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md) method.

You may implement other methods as needed to support the data in your complication. For example, to batch load future timeline entries, implement [`getTimelineEndDate(for:withHandler:)`](./clkcomplicationdatasource/gettimelineenddate%28for,withhandler%29.md) and pass a future date to the handler. For more information, see [Creating complications for your watchOS app](./creating-complications-for-your-watchos-app.md).

> **Note**:  For watchOS 6 and earlier, you must implement both [`getCurrentTimelineEntry(for:withHandler:)`](./clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md) and [`getSupportedTimeTravelDirections(for:withHandler:)`](./clkcomplicationdatasource/getsupportedtimetraveldirections%28for,withhandler%29.md). Use [`getSupportedTimeTravelDirections(for:withHandler:)`](./clkcomplicationdatasource/getsupportedtimetraveldirections%28for,withhandler%29.md) to specify whether your app can batch load future timeline entries.

ClockKit calls your data source methods on your watchOS app’s main thread.

## Topics

### Migrating to WidgetKit
- [var widgetMigrator: any CLKComplicationWidgetMigrator](./clkcomplicationdatasource/widgetmigrator.md)
  A migrator that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationStaticWidgetMigrationConfiguration](./clkcomplicationstaticwidgetmigrationconfiguration.md)
  A configuration object that specifies a static complication in WidgetKit.
- [class CLKComplicationAppIntentWidgetMigrationConfiguration](./clkcomplicationappintentwidgetmigrationconfiguration.md)
  A configuration object that specifies a WidgetKit complication that uses app intents.
- [class CLKComplicationIntentWidgetMigrationConfiguration](./clkcomplicationintentwidgetmigrationconfiguration.md)
  A configuration object that specifies an intents-based complication in WidgetKit.
- [protocol CLKComplicationWidgetMigrator](./clkcomplicationwidgetmigrator.md)
  A protocol that maps ClockKit complications to their WidgetKit replacements.
- [class CLKComplicationWidgetMigrationConfiguration](./clkcomplicationwidgetmigrationconfiguration.md)
  An abstract class that specifies WidgetKit complications.
### Setting information property keys
- [CLKComplicationPrincipalClass](../BundleResources/information-property-list/clkcomplicationprincipalclass.md)
  The name of the class that implements the complication data source protocol.
### Deprecated methods
- [let CLKLaunchedTimelineEntryDateKey: String](./clklaunchedtimelineentrydatekey.md)
  A key that indicates the date when the system launched the complication.
- [let CLKLaunchedComplicationIdentifierKey: String](./clklaunchedcomplicationidentifierkey.md)
  A key that indicates the identifier of a complication the system launched.
- [func getComplicationDescriptors(handler: ([CLKComplicationDescriptor]) -> Void)](./clkcomplicationdatasource/getcomplicationdescriptors%28handler%29.md)
  Returns the list of complication descriptors.
- [func handleSharedComplicationDescriptors([CLKComplicationDescriptor])](./clkcomplicationdatasource/handlesharedcomplicationdescriptors%28_%29.md)
  Informs the app about complications from a shared watch face.
- [func getLocalizableSampleTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./clkcomplicationdatasource/getlocalizablesampletemplate%28for,withhandler%29.md)
  Gets a localizable template that shows sample data for the specified complication.
- [func getPrivacyBehavior(for: CLKComplication, withHandler: (CLKComplicationPrivacyBehavior) -> Void)](./clkcomplicationdatasource/getprivacybehavior%28for,withhandler%29.md)
  Returns the privacy behavior for the specified complication.
- [enum CLKComplicationPrivacyBehavior](./clkcomplicationprivacybehavior.md)
  Constants indicating the complication behavior when the Apple Watch is locked.
- [func getAlwaysOnTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./clkcomplicationdatasource/getalwaysontemplate%28for,withhandler%29.md)
  Returns the template to use during Always On.
- [func getTimelineEndDate(for: CLKComplication, withHandler: (Date?) -> Void)](./clkcomplicationdatasource/gettimelineenddate%28for,withhandler%29.md)
  Retrieves the last date for the data that your app can supply.
- [func getCurrentTimelineEntry(for: CLKComplication, withHandler: (CLKComplicationTimelineEntry?) -> Void)](./clkcomplicationdatasource/getcurrenttimelineentry%28for,withhandler%29.md)
  Retrieves the timeline entry that you want to display now.
- [func getTimelineEntries(for: CLKComplication, after: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Void)](./clkcomplicationdatasource/gettimelineentries%28for,after,limit,withhandler%29.md)
  Retrieves future timeline entries for the complication.
- [func getTimelineAnimationBehavior(for: CLKComplication, withHandler: (CLKComplicationTimelineAnimationBehavior) -> Void)](./clkcomplicationdatasource/gettimelineanimationbehavior%28for,withhandler%29.md)
  Gets the animation behavior when transitioning between timeline entries.
- [enum CLKComplicationTimelineAnimationBehavior](./clkcomplicationtimelineanimationbehavior.md)
  Constants indicating the animation behavior during Time Travel.
- [func getSupportedTimeTravelDirections(for: CLKComplication, withHandler: (CLKComplicationTimeTravelDirections) -> Void)](./clkcomplicationdatasource/getsupportedtimetraveldirections%28for,withhandler%29.md)
  Determines whether your complication can provide timeline entries for the future or the past.
- [struct CLKComplicationTimeTravelDirections](./clkcomplicationtimetraveldirections.md)
  Constants indicating the supported time travel directions, if any.
- [func getTimelineStartDate(for: CLKComplication, withHandler: (Date?) -> Void)](./clkcomplicationdatasource/gettimelinestartdate%28for,withhandler%29.md)
  Retrieves the earliest date for which your complication is prepared to supply data.
- [func getTimelineEntries(for: CLKComplication, before: Date, limit: Int, withHandler: ([CLKComplicationTimelineEntry]?) -> Void)](./clkcomplicationdatasource/gettimelineentries%28for,before,limit,withhandler%29.md)
  Retrieves past timeline entries for the complication.
- [func getNextRequestedUpdateDate(handler: (Date?) -> Void)](./clkcomplicationdatasource/getnextrequestedupdatedate%28handler%29.md)
  Gets the next time at which to update your complication.
- [func requestedUpdateDidBegin()](./clkcomplicationdatasource/requestedupdatedidbegin%28%29.md)
  Indicates that a requested update has begun so that you’ve an opportunity to extend or reload your timeline.
- [func requestedUpdateBudgetExhausted()](./clkcomplicationdatasource/requestedupdatebudgetexhausted%28%29.md)
  Indicates that your complication’s time budget is exhausted.
- [func getPlaceholderTemplate(for: CLKComplication, withHandler: (CLKComplicationTemplate?) -> Void)](./clkcomplicationdatasource/getplaceholdertemplate%28for,withhandler%29.md)
  Gets a static template to display in the selection screen for your complication.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Migration Support
- [Migrating ClockKit complications to WidgetKit](../WidgetKit/converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [let CLKDefaultComplicationIdentifier: String](./clkdefaultcomplicationidentifier.md)
  An identifier representing a default complication.
- [class CLKComplicationDescriptor](./clkcomplicationdescriptor.md)
  A descriptor that defines a complication and the families that it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource)*