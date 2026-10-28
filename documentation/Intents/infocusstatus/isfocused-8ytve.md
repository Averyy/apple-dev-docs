# isFocused

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s preference for receiving communication notifications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- watchOS 8.0+

## Declaration

```swift
@nonobjc
final var isFocused: Bool? { get }
```

## Discussion

When this value is [`true`](../../Swift/true.md), the user doesn’t want notifications to interrupt them. Use this information to display the user’s availability to other people in your communication service.

If the user grants your app access to their focus status, notifications your app receives about communication from important people can break through the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatus/isfocused-8ytve)*