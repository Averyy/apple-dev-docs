# name

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The name of the voice chat channel.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
var name: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * name;
```

## Discussion

Use a unique name for each voice chat channel in your game.

## See Also

### Accessing Properties
- [var players: [GKPlayer]](./players.md)
  The players connected to the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/name)*