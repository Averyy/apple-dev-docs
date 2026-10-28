# HKActivityRingView

**Framework**: HealthKitUI  
**Kind**: class  
**Role**: Class

A view that uses the Move, Exercise, and Stand activity rings to display data from a HealthKit activity summary object.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKActivityRingView
```

```objc
@interface HKActivityRingView : UIView
```

## Mentions

- [Executing Activity Summary Queries](../HealthKit/executing-activity-summary-queries.md)

## Overview

Use [`HKActivityRingView`](./hkactivityringview.md) to display data from an [`HKActivitySummary`](../HealthKit/hkactivitysummary.md) object. For example, the following image shows how the rings can display a summary view of a person’s activity.

![Two partially filled and one completely filled colored concentric rings on a black background.](https://developer.apple.com/tutorials/images/com.apple.healthkit/media-1965751@2x.png)

To display activity summary data from the HealthKit store, use an [`HKActivitySummaryQuery`](../HealthKit/hkactivitysummaryquery.md) object. You can also instantiate and display your own [`HKActivitySummary`](../HealthKit/hkactivitysummary.md) objects, as needed.

The activity ring view always appears as a black rectangle with colored concentric rings. The rings are centered in the view and are sized to fit the available space.

![Two partially filled and one completely filled colored concentric rings centered on a black rectangle background.](https://developer.apple.com/tutorials/images/com.apple.healthkit/media-1965753@2x.png)

The activity ring view displays different rings depending on the properties defined in the ring view’s [`HKActivitySummary`](../HealthKit/hkactivitysummary.md) property. When the view’s [`HKActivitySummary`](../HealthKit/hkactivitysummary.md) has [`activityMoveMode`](../HealthKit/hkactivitymovemodeobject/activitymovemode.md) set to [`appleMoveTime`](../HealthKit/hkactivitysummary/applemovetime.md) and `nil` values for [`appleExerciseTimeGoal`](../HealthKit/hkactivitysummary/appleexercisetimegoal.md) and [`appleStandHoursGoal`](../HealthKit/hkactivitysummary/applestandhoursgoal.md) the ring only displays the red Move ring. Otherwise, it displays the Move, Exercise, and Stand activity as red, green, and blue concentric rings. Summary data from the HealthKit store only displays the Move ring when the person hasn’t paired an Apple Watch.

The rings can display as either empty or with a dot at the top of the ring to display a lack of data. Empty rings indicate that the activity summary is missing, and a dot at the top indicates that the activity summary’s values are set to zero.

If the ring has a `nil`-valued `activitySummary` quantity properties, the rings appear empty. Use this to indicate that there is no summary data available for the specified day. For example, dates in the future.

![Three dimly colored concentric rings.](https://developer.apple.com/tutorials/images/com.apple.healthkit/media-2556410@2x.png)

If the summary has zero-valued quantities set for its value properties, the ring displays a dot at the top of the ring. Use this to indicate that the person hasn’t burned any active calories, exercised, or earned any stand hours for the specified day.

![Three dimly colored concentric rings with a bright dot at the top of each ring.](https://developer.apple.com/tutorials/images/com.apple.healthkit/media-2556419@2x.png)

To display data for a ring, the [`HKActivitySummary`](../HealthKit/hkactivitysummary.md) object must have a non-`nil` quantity for both the corresponding value property and the goal property.

| Ring | Value property | Goal property |
| --- | --- | --- |
| Move | [`activeEnergyBurned`](../HealthKit/hkactivitysummary/activeenergyburned.md) | [`activeEnergyBurnedGoal`](../HealthKit/hkactivitysummary/activeenergyburnedgoal.md) |
| Exercise | [`appleExerciseTime`](../HealthKit/hkactivitysummary/appleexercisetime.md) | [`appleExerciseTimeGoal`](../HealthKit/hkactivitysummary/appleexercisetimegoal.md) |
| Stand | [`appleStandHours`](../HealthKit/hkactivitysummary/applestandhours.md) | [`appleStandHoursGoal`](../HealthKit/hkactivitysummary/applestandhoursgoal.md) |

Move only ring properties:

| Ring | Value property | Goal property |
| --- | --- | --- |
| Move | [`appleMoveTime`](../HealthKit/hkactivitysummary/applemovetime.md) | [`activeEnergyBurned`](../HealthKit/hkactivitysummary/activeenergyburned.md) | [`appleMoveTimeGoal`](../HealthKit/hkactivitysummary/applemovetimegoal.md) | [`activeEnergyBurnedGoal`](../HealthKit/hkactivitysummary/activeenergyburnedgoal.md) |

The activity ring view colors a percentage of each ring based on these properties, as shown here:

```objc
ring percent = value property quantity / goal property quantity
```

![One partially filled colored concentric ring on a black background.](https://developer.apple.com/tutorials/images/com.apple.healthkit/single-ring@2x.png)

The following code snippet shows how to manually display only the Move ring:

```swift
let moveOnlySummary = HKActivitySummary()
moveOnlySummary.activityMoveMode = .appleMoveTime
moveOnlySummary.appleMoveTime = HKQuantity(unit: .minute(), doubleValue: 60.0)
moveOnlySummary.appleMoveTimeGoal = HKQuantity(unit: .minute(), doubleValue: 90.0)
```

## Topics

### Setting the activity summary
- [var activitySummary: HKActivitySummary?](./hkactivityringview/activitysummary.md)
  The active summary displayed by the activity ring view.
- [func setActivitySummary(HKActivitySummary?, animated: Bool)](./hkactivityringview/setactivitysummary%28_,animated%29.md)
  Sets the activity summary displayed by the activity ring view.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkitui/hkactivityringview)*