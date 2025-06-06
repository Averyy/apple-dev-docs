# fileLabelColors

**Framework**: AppKit  
**Kind**: property

The array of colors for the file labels.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var fileLabelColors: [NSColor] { get }
```

#### Return Value

An array of `NSColor` objects.

#### Discussion

This array has the same number of elements as [`fileLabels`](nsworkspace/filelabels.md), and the color at a given index corresponds to the label at the same index.

You can listen for notifications named [`didChangeFileLabelsNotification`](nsworkspace/didchangefilelabelsnotification.md) to be notified when file labels change that may result in changes to the order of the `fileLabelColors`.

You can safely call this method from any thread of your app.

## See Also

- [var fileLabels: [String]](nsworkspace/filelabels.md)
  The array of file labels, returned as strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/filelabelcolors)*