# participants

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The recipient of the user’s call request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var participants: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * participants;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * participants;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordfilter/participants)*