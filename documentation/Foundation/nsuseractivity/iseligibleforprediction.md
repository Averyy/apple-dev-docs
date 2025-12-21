# isEligibleForPrediction

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether Siri can suggest the user activity as a shortcut to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var isEligibleForPrediction: Bool { get set }
```

#### Discussion

To donate a user activity to Siri Shortcuts, set [`isEligibleForPrediction`](nsuseractivity/iseligibleforprediction.md) to [`true`](https://developer.apple.com/documentation/Swift/true) and make the user activity current. To make the user activity current, call the activity’s [`becomeCurrent()`](nsuseractivity/becomecurrent().md) method, or assign it to the [`userActivity`](https://developer.apple.com/documentation/UIKit/UIResponder/userActivity) property on a [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) or [`UIResponder`](https://developer.apple.com/documentation/UIKit/UIResponder) object. For more information, see [`Donating Shortcuts`](https://developer.apple.com/documentation/SiriKit/donating-shortcuts).

## See Also

- [var suggestedInvocationPhrase: String?](nsuseractivity/suggestedinvocationphrase.md)
  A phrase suggested to the user when they create a shortcut.
- [var shortcutAvailability: INShortcutAvailabilityOptions](nsuseractivity/shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforprediction)*