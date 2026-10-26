# caller

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The person who participated in the call with the current user.

**Availability**:
- iOS 11.0+ - Deprecated in 14.5
- iPadOS 11.0+ - Deprecated in 14.5
- Mac Catalyst 13.1+ - Deprecated in 14.5
- macOS 12.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 7.3

## Declaration

```swift
@NSCopying
var caller: INPerson? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPerson * caller;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPerson * caller;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/caller)*