# invalidate()

**Framework**: AudioAccessoryKit  
**Kind**: method  
**Required**: Yes

Called when the head-tracking session has been invalidated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func invalidate()
```

#### Discussion

After this is called, no further state updates will be delivered on this handler, and the session is no longer valid for forwarding sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler/invalidate())*