# id

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

A stable, unique identifier for the session these attributes describe.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var id: String { get }
```

#### Discussion

The system uses this value to match session lifecycle events (start, update, end) and to route push tokens to the correct session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionattributes/id)*