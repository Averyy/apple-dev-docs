# FocusFilterAppContext

**Framework**: App Intents  
**Kind**: struct

A type that contains app-specific contextual information for a particular Focus, such as the notification filter criteria to apply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct FocusFilterAppContext
```

## Topics

### Creating the app context
- [init(notificationFilterPredicate: NSPredicate?)](focusfilterappcontext/init(notificationfilterpredicate:).md)
  Creates a `FocusFilterAppContext` with a specified `notificationFilterPredicate`
### Getting the filter predicate
- [let notificationFilterPredicate: NSPredicate?](focusfilterappcontext/notificationfilterpredicate.md)
  An `NSPredicate` for system to filter the user’s notifications of the app when a Focus is active.
### Initializers
- [init(notificationFilterPredicate: NSPredicate?, targetContentIdentifierPrefix: String?)](focusfilterappcontext/init(notificationfilterpredicate:targetcontentidentifierprefix:).md)
  Creates a focus filter context with a specified predicate and identifier prefix.
### Instance Properties
- [let targetContentIdentifierPrefix: String?](focusfilterappcontext/targetcontentidentifierprefix.md)
  An identifier you provide to the system for use in scheme prefixes for Focus.

## See Also

- [protocol SetFocusFilterIntent](setfocusfilterintent.md)
  An interface for providing an app intent that you use to adapt your app’s behavior when Focus changes.
- [Defining your app’s Focus filter](focus/defining_your_app_s_focus_filter.md)
  Customize your app’s behavior to reflect the device’s current Focus.
- [struct FocusFilterSuggestionContext](focusfiltersuggestioncontext.md)
  A type you use to suggest app configurations for a given Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/focusfilterappcontext)*