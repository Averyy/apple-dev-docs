# SetFocusFilterIntent

**Framework**: Appintents  
**Kind**: protocol

An interface for providing an app intent that you use to adapt your app’s behavior when Focus changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol SetFocusFilterIntent : AppIntent, InstanceDisplayRepresentable
```

#### Overview

> **Note**:  Session 10121: [`Meet Focus filters`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10121).

## Topics

### Getting the current app configuration
- [static var current: Self](setfocusfilterintent/current.md)
- [static func suggestedFocusFilters(for: FocusFilterSuggestionContext) async -> [Self]](setfocusfilterintent/suggestedfocusfilters(for:).md)
  You can implement this method to return a list of suggested focus configurations. This is useful when the suggested focus configurations are different from the configuration when the focus is turned off.
### Configuring app context for the Focus
- [var appContext: FocusFilterAppContext](setfocusfilterintent/appcontext.md)
  An app context that is associated with the focus configuration. The system will retrieve this app context and adapt the system behavior based on the context provided.
- [static func invalidateFocusFilterAppContext()](setfocusfilterintent/invalidatefocusfilterappcontext.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Defining your app’s Focus filter](focus/defining_your_app_s_focus_filter.md)
  Customize your app’s behavior to reflect the device’s current Focus.
- [struct FocusFilterAppContext](focusfilterappcontext.md)
  A type that contains app-specific contextual information for a particular Focus, such as the notification filter criteria to apply.
- [struct FocusFilterSuggestionContext](focusfiltersuggestioncontext.md)
  A type you use to suggest app configurations for a given Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents/setfocusfilterintent)*