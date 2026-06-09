# interaction

**Framework**: Foundation  
**Kind**: property

The SiriKit interaction object to use when configuring your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var interaction: INInteraction? { get }
```

#### Discussion

When SiriKit launches your app, it fills this property with the intent and response information that are the reason for launching your app. Use the information in this property to configure your app’s interface and show any relevant interaction details. If your app wasn’t launched because of a Siri interaction, the value in this property is `nil`.

## See Also

- [var suggestedInvocationPhrase: String?](nsuseractivity/suggestedinvocationphrase.md)
  A phrase suggested to the user when they create a shortcut.
- [var shortcutAvailability: INShortcutAvailabilityOptions](nsuseractivity/shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/interaction)*