# eraseProgressPanelDidFinish(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Notification sent by the panel after ordering out.

**Availability**:
- macOS ?+

## Declaration

```swift
func eraseProgressPanelDidFinish(_ aNotification: Notification!)
```

#### Discussion

If the delegate implements this method it will receive the message after the panel is removed from display.

## Parameters

- `aNotification`: Always     You can retrieve the   object in question by sending   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:))*