# shortcutAvailability

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

When you donate an activity, include a set of relevant doc://com.apple.documentation/documentation/sirikit/inshortcutavailabilityoptions to describe appropriate categories for offering a shortcut to the activity.

If none of the availability options apply to your intent, use the empty set. The empty set is the default value for this property.

> **Note**:  To access the `suggestedInvocationPhrase` property, import the Intents framework.

 To access the `suggestedInvocationPhrase` property, import the Intents framework.

## See Also

- [var isEligibleForPrediction: Bool](nsuseractivity/iseligibleforprediction.md)
  A Boolean value that determines whether Siri can suggest the user activity as a shortcut to the user.
- [var suggestedInvocationPhrase: String?](nsuseractivity/suggestedinvocationphrase.md)
  A phrase suggested to the user when they create a shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/shortcutavailability)*