# burnProgressPanelDidFinish(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Notification sent by the panel after ordering out.

**Availability**:
- macOS

## Declaration

```swift
func burnProgressPanelDidFinish(_ aNotification: Notification!)
```

```objc
- (void) burnProgressPanelDidFinish:(NSNotification *) aNotification;
```

#### Discussion

If the delegate implements this method it will receive the message after the panel is removed from display.

## Parameters

- `aNotification`: 	Always `DRBurnProgressPanelDidFinishNotification`


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish(_:))*