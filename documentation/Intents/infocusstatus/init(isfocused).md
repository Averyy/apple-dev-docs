# init(isFocused:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object that indicates the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- watchOS 8.0+

## Declaration

```swift
@nonobjc
convenience init(isFocused: Bool? = nil)
```

#### Return Value

A new status object, or `nil` if the system can’t create one.

## Parameters

- `isFocused`: The user’s preference for receiving notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatus/init(isfocused:))*