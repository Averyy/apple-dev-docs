# isEnabled

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

State of the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isEnabled) BOOL enabled;
```

#### Discussion

Triggers that are not enabled never fire.

## See Also

### Managing Triggers
- [var name: String](./name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](./enable%28_,completionhandler%29.md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](./lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for this trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/isenabled)*