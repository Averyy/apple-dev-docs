# suggestedInvocationPhrase

**Framework**: Foundation  
**Kind**: property

A phrase suggested to the user when they create a shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var suggestedInvocationPhrase: String? { get set }
```

#### Discussion

The system displays the suggested invocation phrase to the user when they create the shortcut. Use a short, memorable phrase, such as “Soup time”.

![A screenshot of adding a shortcut to Siri for one order of tomato soup.](https://docs-assets.developer.apple.com/published/8ba32c1cccce9885aad9bc8ebc40e79e/media-3020431%402x.png)

> **Note**:  To access the [`suggestedInvocationPhrase`](nsuseractivity/suggestedinvocationphrase.md) property, import the  framework.

## See Also

- [var isEligibleForPrediction: Bool](nsuseractivity/iseligibleforprediction.md)
  A Boolean value that determines whether Siri can suggest the user activity as a shortcut to the user.
- [var shortcutAvailability: INShortcutAvailabilityOptions](nsuseractivity/shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/suggestedinvocationphrase)*