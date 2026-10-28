# shortcutAvailability

**Framework**: Intents  
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

When you donate an intent, include a set of relevant [`INShortcutAvailabilityOptions`](../inshortcutavailabilityoptions.md) options to describe appropriate situations for offering a shortcut to the intent.

If none of the availability options apply to your intent, use the empty set. The empty set is the default value for this property.

## See Also

### Accessing Intent Information
- [var identifier: String?](./identifier.md)
  The unique identifier for this intent object.
- [var intentDescription: String?](./intentdescription.md)
  A string describing the content of the intent.
- [var suggestedInvocationPhrase: String?](./suggestedinvocationphrase.md)
  The intent’s display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintent/shortcutavailability)*