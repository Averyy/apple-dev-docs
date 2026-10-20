# CMFallDetectionDelegate

**Framework**: Core Motion  
**Kind**: protocol  
**Role**: Protocol

A delegate that receives information about fall detection events and authorization status changes.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
protocol CMFallDetectionDelegate : NSObjectProtocol
```

```objc
@protocol CMFallDetectionDelegate <NSObject>
```

## Topics

### Detecting Falls
- [func fallDetectionManager(CMFallDetectionManager, didDetect: CMFallDetectionEvent, completionHandler: () -> Void)](./cmfalldetectiondelegate/falldetectionmanager%28_,diddetect,completionhandler%29.md)
  Indicates a fall detection event occurred.
### Detecting Authorization Changes
- [func fallDetectionManagerDidChangeAuthorization(CMFallDetectionManager)](./cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization%28_%29.md)
  Indicates the fall detection authorization status changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Fall detection
- [class CMFallDetectionManager](./cmfalldetectionmanager.md)
  An object for managing fall detection events.
- [class CMFallDetectionEvent](./cmfalldetectionevent.md)
  An object that contains data about a fall detection event.
- [NSFallDetectionUsageDescription](../BundleResources/information-property-list/nsfalldetectionusagedescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate)*