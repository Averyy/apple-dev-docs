# init(intent:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a shortcut with the specified intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 11.0+
- watchOS 5.0+

## Declaration

```swift
init?(intent: INIntent)
```

## Discussion

Returns `nil` for invalid intents.

## Parameters

- `intent`: The intent to perform when invoking the shortcut. The intent must have a title and be a valid shortcut type.

## See Also

### Creating a Shortcut
- [init(userActivity: NSUserActivity)](./init%28useractivity%29.md)
  Creates a shortcut with the specified user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcut-swift.enum/init(intent:))*