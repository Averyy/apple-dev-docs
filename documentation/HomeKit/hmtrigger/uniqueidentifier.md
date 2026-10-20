# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for this trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniqueIdentifier: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * uniqueIdentifier;
```

## See Also

### Managing Triggers
- [var name: String](./name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the trigger.
- [var isEnabled: Bool](./isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](./enable%28_,completionhandler%29.md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](./lastfiredate.md)
  The last time this trigger fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/uniqueidentifier)*