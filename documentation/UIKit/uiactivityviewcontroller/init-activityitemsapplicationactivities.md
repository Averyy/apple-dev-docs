# init(activityItems:applicationActivities:)

**Framework**: UIKit  
**Kind**: init

Initializes a new activity view controller object that acts on the specified data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(activityItems: [Any], applicationActivities: [UIActivity]?)
```

#### Return Value

The activity view controller to present.

#### Discussion

It is your responsibility to present and dismiss the view controller using the appropriate means for the given device idiom. On iPad, you must present the view controller in a popover. On other devices, you must present it modally.

## Parameters

- `activityItems`: This array must not be   and must contain at least one object.
- `applicationActivities`: An array of   objects representing the custom services that your application supports. This parameter may be  .

## See Also

- [convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)](uiactivityviewcontroller/init(activityitemsconfiguration:).md)
  Initializes a new activity view controller object that acts on the specified configuration.
- [class UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)
  A configuration that allows a responder to export data through a variety of interactions.
- [protocol UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)
  A set of methods adopted by an object so that the object can act as an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/init(activityitems:applicationactivities:))*