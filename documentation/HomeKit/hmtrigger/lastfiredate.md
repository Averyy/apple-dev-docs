# lastFireDate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The last time this trigger fired.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 10.0

> **Deprecated**: This property is no longer supported.

## Declaration

```swift
var lastFireDate: Date? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * lastFireDate;
```

#### Discussion

`nil` if the trigger has never fired.

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
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/lastfiredate)*