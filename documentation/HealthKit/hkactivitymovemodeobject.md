# HKActivityMoveModeObject

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An object that contains a movement mode value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class HKActivityMoveModeObject
```

```objc
@interface HKActivityMoveModeObject : NSObject
```

## Topics

### Accessing the data
- [var activityMoveMode: HKActivityMoveMode](./hkactivitymovemodeobject/activitymovemode.md)
  A property that contains the movement mode value.
### Initializers
- [init?(coder: NSCoder)](./hkactivitymovemodeobject/init%28coder%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Activity rings
- [class HKActivitySummary](./hkactivitysummary.md)
  An object that contains the move, exercise, and stand data for a given day.
- [struct HKActivitySummaryQueryDescriptor](./hkactivitysummaryquerydescriptor.md)
  A query interface that reads activity summaries using Swift concurrency.
- [class HKActivitySummaryQuery](./hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [class HKActivityRingView](../HealthKitUI/hkactivityringview.md)
  A view that uses the Move, Exercise, and Stand activity rings to display data from a HealthKit activity summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitymovemodeobject)*