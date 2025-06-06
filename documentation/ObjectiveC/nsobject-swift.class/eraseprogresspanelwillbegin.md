# eraseProgressPanelWillBegin(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Notification sent by the panel before display.

**Availability**:
- macOS ?+

## Declaration

```swift
func eraseProgressPanelWillBegin(_ aNotification: Notification!)
```

#### Discussion

If the delegate implements this method it will receive the message immediately before the panel is displayed.

## Parameters

- `aNotification`: Always     You can retrieve the   object in question by sending   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanelwillbegin(_:))*