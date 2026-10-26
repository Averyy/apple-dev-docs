# recipient

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The person involved in the call.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var recipient: INPerson? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPerson * recipient;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPerson * recipient;
```

#### Discussion

This property represents the person with whom the call occurred. Use this property to limit your search only to records containing the specified person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/recipient)*