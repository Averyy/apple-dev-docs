# initWithIsFocused:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates an object that indicates the user’s ability to receive communication notifications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (instancetype) initWithIsFocused:(NSNumber *) isFocused;
```

#### Return Value

A new status object, or `nil` if the system can’t create one.

## Parameters

- `isFocused`: The user’s preference for receiving notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatus/initwithisfocused:)*