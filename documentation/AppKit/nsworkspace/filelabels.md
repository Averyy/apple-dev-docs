# fileLabels

**Framework**: AppKit  
**Kind**: property

The array of file labels, returned as strings.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var fileLabels: [String] { get }
```

#### Return Value

An array of strings.

#### Discussion

You can listen for notifications named [`didChangeFileLabelsNotification`](nsworkspace/didchangefilelabelsnotification.md) to be notified when file labels change.

You can safely call this method from any thread of your app.

## See Also

- [var fileLabelColors: [NSColor]](nsworkspace/filelabelcolors.md)
  The array of colors for the file labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/filelabels)*