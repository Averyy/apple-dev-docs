# CPPointOfInterestTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The methods to handle a point of interest template’s events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
protocol CPPointOfInterestTemplateDelegate : NSObjectProtocol
```

```objc
@protocol CPPointOfInterestTemplateDelegate <NSObject>
```

## Overview

You use the `CPPointOfInterestTemplateDelegate` protocol to respond to a point of interest template’s events. The protocol defines methods that CarPlay calls in response to these events, and your implementation provides the appropriate behavior for when the events occur. For example, when the user pans the template’s map and the visible region changes, update the points of interest that the template displays to only those relevant to the new region.

## Topics

### Responding to map region changes
- [func pointOfInterestTemplate(CPPointOfInterestTemplate, didChangeMapRegion: MKCoordinateRegion)](./cppointofinteresttemplatedelegate/pointofinteresttemplate%28_,didchangemapregion%29.md)
  Tells the delegate about changes to the visible region of the template’s map.
### Responding to a point of interest selection
- [func pointOfInterestTemplate(CPPointOfInterestTemplate, didSelectPointOfInterest: CPPointOfInterest)](./cppointofinteresttemplatedelegate/pointofinteresttemplate%28_,didselectpointofinterest%29.md)
  Tells the delegate when the user selects a point of interest.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling events
- [var pointOfInterestDelegate: (any CPPointOfInterestTemplateDelegate)?](./cppointofinteresttemplate/pointofinterestdelegate.md)
  The object that serves as the template’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplatedelegate)*