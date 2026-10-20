# guestIdentifier

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A developer-created string that identifies a guest player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var guestIdentifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSString * guestIdentifier;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSString * guestIdentifier;
```

## See Also

### Creating a guest player
- [class func anonymousGuestPlayer(withIdentifier: String) -> Self](./anonymousguestplayer%28withidentifier%29.md)
  Creates a guest player with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/guestidentifier)*