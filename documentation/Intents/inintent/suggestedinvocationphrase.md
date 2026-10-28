# suggestedInvocationPhrase

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The intent’s display name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var suggestedInvocationPhrase: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * suggestedInvocationPhrase;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * suggestedInvocationPhrase;
```

## Mentions

- [Donating Reservations](../../SiriKit/donating-reservations.md)
- [Donating Shortcuts](../../SiriKit/donating-shortcuts.md)

## Discussion

Suggest a short, memorable phrase the user might say to activate this shortcut.

## See Also

### Accessing Intent Information
- [var identifier: String?](./identifier.md)
  The unique identifier for this intent object.
- [var intentDescription: String?](./intentdescription.md)
  A string describing the content of the intent.
- [var shortcutAvailability: INShortcutAvailabilityOptions](./shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintent/suggestedinvocationphrase)*