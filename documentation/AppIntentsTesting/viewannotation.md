# ViewAnnotation

**Framework**: App Intents Testing  
**Kind**: struct

The onscreen context you provide to the system by annotating a view with an app entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ViewAnnotation
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

Use the `ViewAnnotation` structure to test whether the currently visible user interface and its views have the expected entity view annotations you created to provide onscreen context to the system. Retrieve visible view annotations using [`viewAnnotations()`](appentitydefinition/viewannotations().md), then inspect their selection state and which entities are visible on-screen.

## Topics

### Accessing onscreen context
- [let entity: AnyAppEntity](viewannotation/entity.md)
  The underlying app entity data.
- [let isSelected: Bool](viewannotation/isselected.md)
  A Boolean value that indicates whether the entity’s associated view is selected.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/viewannotation)*