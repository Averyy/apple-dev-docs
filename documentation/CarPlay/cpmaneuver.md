# CPManeuver

**Framework**: CarPlay  
**Kind**: class

An object that describes a single navigation instruction.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPManeuver
```

#### Overview

You use maneuvers to provide turn-by-turn guidance in navigation apps. Each maneuver represents a single navigation instruction and can include a symbol, an instruction, and estimates for remaining time and distance.

You supply an instruction as an array of variants, each with a different length. CarPlay chooses the longest variant that best fits the available space on the screen. You can optionally provide attributed variants that embed images using [`NSTextAttachment`](https://developer.apple.com/documentation/UIKit/NSTextAttachment). See [`attributedInstructionVariants`](cpmaneuver/attributedinstructionvariants.md) for more information.

In addition to the route guidance panel, you can show maneuvers on the CarPlay dashboard or in notification banners. Use the relevant properties to provide context-specific instructions and images.

## Topics

### Providing instructions
- [var instructionVariants: [String]](cpmaneuver/instructionvariants.md)
  An array of instruction variants for the maneuver.
- [var dashboardInstructionVariants: [String]](cpmaneuver/dashboardinstructionvariants.md)
  An array of instruction variants for the CarPlay dashboard.
- [var notificationInstructionVariants: [String]](cpmaneuver/notificationinstructionvariants.md)
  An array of instruction variants for notification banners.
### Providing attributed instructions
- [var attributedInstructionVariants: [NSAttributedString]](cpmaneuver/attributedinstructionvariants.md)
  An array of attributed instruction variants for the maneuver.
- [var dashboardAttributedInstructionVariants: [NSAttributedString]](cpmaneuver/dashboardattributedinstructionvariants.md)
  An array of attributed instruction variants for the CarPlay dashboard.
- [var notificationAttributedInstructionVariants: [NSAttributedString]](cpmaneuver/notificationattributedinstructionvariants.md)
  An array of attributed instruction variants for notification banners.
### Providing travel estimates
- [var initialTravelEstimates: CPTravelEstimates?](cpmaneuver/initialtravelestimates.md)
  An object that describes the distance and time remaining before the maneuver completes.
### Providing symbol images
- [var symbolImage: UIImage?](cpmaneuver/symbolimage.md)
  An image that represents the maneuver.
- [var dashboardSymbolImage: UIImage?](cpmaneuver/dashboardsymbolimage.md)
  An image for the CarPlay dashboard that represents the maneuver.
- [var notificationSymbolImage: UIImage?](cpmaneuver/notificationsymbolimage.md)
  An image for notification banners that represents the maneuver.
- [var symbolSet: CPImageSet?](cpmaneuver/symbolset.md)
  An image set that represents the maneuver.
### Providing junction images
- [var junctionImage: UIImage?](cpmaneuver/junctionimage.md)
  An image that represents an upcoming junction.
- [var dashboardJunctionImage: UIImage?](cpmaneuver/dashboardjunctionimage.md)
  An image for the CarPlay dashboard that represents an upcoming junction.
### Providing junction information
- [var junctionType: CPJunctionType](cpmaneuver/junctiontype.md)
  A value that represents the type of junction associated with this maneuver.
- [var junctionExitAngle: Measurement<UnitAngle>?](cpmaneuver/junctionexitangle.md)
  The angle of the exit road of this junction.
- [var junctionElementAngles: Set<Measurement<UnitAngle>>?](cpmaneuver/junctionelementangles.md)
  A set of angles for the rest of the roads of this junction.
### Providing maneuver information
- [var maneuverType: CPManeuverType](cpmaneuver/maneuvertype.md)
  A value that represents the type of maneuver.
- [var roadFollowingManeuverVariants: [String]?](cpmaneuver/roadfollowingmaneuvervariants.md)
  An array of strings that represent the names of the road following this maneuver, arranged from most to least preferred.
- [var linkedLaneGuidance: CPLaneGuidance](cpmaneuver/linkedlaneguidance.md)
  A value that represents lane guidance associated with this maneuver.
- [var highwayExitLabel: String](cpmaneuver/highwayexitlabel.md)
  A string that describes a highway exit.
- [var trafficSide: CPTrafficSide](cpmaneuver/trafficside.md)
  A value that represents which side of the road the traffic drives on.
### Providing additional information
- [var userInfo: Any?](cpmaneuver/userinfo.md)
  A custom object associated with the maneuver.
### Instance properties
- [var cardBackgroundColor: UIColor?](cpmaneuver/cardbackgroundcolor.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [enum CPManeuverState](cpmaneuverstate.md)
  Values that describe the state of a maneuver.
- [enum CPManeuverType](cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver)*