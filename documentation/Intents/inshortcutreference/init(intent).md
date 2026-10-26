# init(intent:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a shortcut with the specified intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init?(intent: INIntent)
```

```objc
- (instancetype) initWithIntent:(INIntent *) intent;
```

#### Return Value

A new shortcut object if the specified intent is valid; otherwise, returns `nil`.

## Parameters

- `intent`: The intent to perform when invoking the shortcut. The intent must have a title and be a valid shortcut type.

## See Also

### Creating a Shortcut
- [init(userActivity: NSUserActivity)](./init%28useractivity%29.md)
  Creates a shortcut with the specified user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutreference/init(intent:))*