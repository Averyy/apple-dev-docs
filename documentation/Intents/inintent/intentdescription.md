# intentDescription

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A string describing the content of the intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var intentDescription: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * intentDescription;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * intentDescription;
```

## See Also

### Accessing Intent Information
- [var identifier: String?](./identifier.md)
  The unique identifier for this intent object.
- [var suggestedInvocationPhrase: String?](./suggestedinvocationphrase.md)
  The intent’s display name.
- [var shortcutAvailability: INShortcutAvailabilityOptions](./shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintent/intentdescription)*