# contacts

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The users to call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
var contacts: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * contacts;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * contacts;
```

#### Discussion

Use the information in each [`INPerson`](../inperson.md) object to look for a matching contact in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintent/contacts)*