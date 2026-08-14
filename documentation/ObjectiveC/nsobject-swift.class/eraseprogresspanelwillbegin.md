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

- `aNotification`: Always `DREraseProgressPanelWillBeginNotification` You can retrieve the `DREraseProgressPanel` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/object) to `aNotification`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanelwillbegin(_:))*