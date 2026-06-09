# beginRefreshing()

**Framework**: AppKit  
**Kind**: method

Tells the refresh controller that a refresh operation has begun.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func beginRefreshing()
```

#### Discussion

Call this method to programmatically start a refresh operation. The refresh controller enters the refreshing state and displays its activity indicator. This is typically used when you want to show a refresh initiated by something other than user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrefreshcontroller/beginrefreshing())*