# CFNotificationSuspensionBehavior.drop

**Framework**: Core Foundation  
**Kind**: case

The server will not queue any notifications of the specified name and object while the receiving application is in the background.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case drop
```

## See Also

- [CFNotificationSuspensionBehavior.coalesce](cfnotificationsuspensionbehavior/coalesce.md)
  The server will only queue the last notification of the specified name and object; earlier notifications are dropped.
- [CFNotificationSuspensionBehavior.hold](cfnotificationsuspensionbehavior/hold.md)
  The server will hold all matching notifications until the queue has been filled (queue size determined by the server) at which point the server may flush queued notifications.
- [CFNotificationSuspensionBehavior.deliverImmediately](cfnotificationsuspensionbehavior/deliverimmediately.md)
  The server will deliver notifications of the specified name and object whether or not the application is in the background. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior/drop)*