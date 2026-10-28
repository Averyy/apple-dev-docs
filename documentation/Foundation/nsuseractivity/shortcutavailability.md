# shortcutAvailability

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A set of defined contexts in which an intent or activity might be relevant to a user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var shortcutAvailability: INShortcutAvailabilityOptions { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INShortcutAvailabilityOptions shortcutAvailability;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INShortcutAvailabilityOptions shortcutAvailability;
```

## Discussion

When you donate an activity, include a set of relevant [`INShortcutAvailabilityOptions`](../../Intents/inshortcutavailabilityoptions.md) to describe appropriate categories for offering a shortcut to the activity.

If none of the availability options apply to your intent, use the empty set. The empty set is the default value for this property.

> **Note**:  To access the `suggestedInvocationPhrase` property, import the Intents framework.

## See Also

### Providing SiriKit with activity details
- [var interaction: INInteraction?](./interaction.md)
  The SiriKit interaction object to use when configuring your app.
- [var suggestedInvocationPhrase: String?](./suggestedinvocationphrase.md)
  A phrase suggested to the user when they create a shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/shortcutavailability)*