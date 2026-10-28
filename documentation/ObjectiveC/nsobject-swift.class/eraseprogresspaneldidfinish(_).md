# eraseProgressPanelDidFinish(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Notification sent by the panel after ordering out.

**Availability**:
- macOS

## Declaration

```swift
func eraseProgressPanelDidFinish(_ aNotification: Notification!)
```

```objc
- (void) eraseProgressPanelDidFinish:(NSNotification *) aNotification;
```

## Discussion

If the delegate implements this method it will receive the message after the panel is removed from display.

## Parameters

- `aNotification`: Always `DREraseProgressPanelDidFinishNotification` You can retrieve the `DREraseProgressPanel` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `aNotification`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:))*