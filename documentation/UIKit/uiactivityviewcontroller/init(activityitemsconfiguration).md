# init(activityItemsConfiguration:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new activity view controller object that acts on the specified configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)
```

```objc
- (instancetype) initWithActivityItemsConfiguration:(id<UIActivityItemsConfigurationReading>) activityItemsConfiguration;
```

## See Also

### Initializing the activity view controller
- [init(activityItems: [Any], applicationActivities: [UIActivity]?)](./init%28activityitems,applicationactivities%29.md)
  Initializes a new activity view controller object that acts on the specified data.
- [class UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md)
  A configuration that allows a responder to export data through a variety of interactions.
- [protocol UIActivityItemsConfigurationReading](../uiactivityitemsconfigurationreading.md)
  A set of methods adopted by an object so that the object can act as an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/init(activityitemsconfiguration:))*