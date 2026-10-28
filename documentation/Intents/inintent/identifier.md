# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier for this intent object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * identifier;
```

## Discussion

SiriKit generates a UUID for this property at creation time and it can’t be changed later. You can use this value in your app to identify the specific request made by the user.

## See Also

### Accessing Intent Information
- [var intentDescription: String?](./intentdescription.md)
  A string describing the content of the intent.
- [var suggestedInvocationPhrase: String?](./suggestedinvocationphrase.md)
  The intent’s display name.
- [var shortcutAvailability: INShortcutAvailabilityOptions](./shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintent/identifier)*