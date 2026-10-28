# init(userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a shortcut with the specified user activity.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(userActivity: NSUserActivity)
```

```objc
- (instancetype) initWithUserActivity:(NSUserActivity *) userActivity;
```

## Return Value

A new shortcut object initialized with the specified user activitiy.

## Parameters

- `userActivity`: The user activity indicating the action to perform when invoking the shortcut.

## See Also

### Creating a Shortcut
- [init?(intent: INIntent)](./init%28intent%29.md)
  Creates a shortcut with the specified intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutreference/init(useractivity:))*