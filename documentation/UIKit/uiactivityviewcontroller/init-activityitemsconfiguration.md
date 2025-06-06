# init(activityItemsConfiguration:)

**Framework**: UIKit  
**Kind**: init

Initializes a new activity view controller object that acts on the specified configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)
```

## See Also

- [init(activityItems: [Any], applicationActivities: [UIActivity]?)](uiactivityviewcontroller/init(activityitems:applicationactivities:).md)
  Initializes a new activity view controller object that acts on the specified data.
- [class UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)
  A configuration that allows a responder to export data through a variety of interactions.
- [protocol UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)
  A set of methods adopted by an object so that the object can act as an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/init(activityitemsconfiguration:))*