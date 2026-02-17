# init(labels:trackingMode:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a standard segmented control containing one segment for each of the provided labels.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(labels: [String], trackingMode: NSSegmentedControl.SwitchTracking, target: Any?, action: Selector?)
```

#### Return Value

An initialized segmented control.

## Parameters

- `labels`: An array of localized label strings to use for the control’s segments.
- `trackingMode`: The selection mode for the control. The NSSegmentSwitchTracking enum describes the possible values and their effects.
- `target`: The target object that receives action messages from the control.
- `action`: The action message sent by the control.

## See Also

- [convenience init(images: [NSImage], trackingMode: NSSegmentedControl.SwitchTracking, target: Any?, action: Selector?)](nssegmentedcontrol/init(images:trackingmode:target:action:).md)
  Creates a standard segmented control containing one segment for each of the provided images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/init(labels:trackingmode:target:action:))*