# fileLabelColors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of colors for the file labels.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var fileLabelColors: [NSColor] { get }
```

```objc
@property (copy, readonly) NSArray<NSColor *> * fileLabelColors;
```

#### Return Value

An array of `NSColor` objects.

#### Discussion

This array has the same number of elements as [`fileLabels`](./filelabels.md), and the color at a given index corresponds to the label at the same index.

You can listen for notifications named [`didChangeFileLabelsNotification`](./didchangefilelabelsnotification.md) to be notified when file labels change that may result in changes to the order of the `fileLabelColors`.

You can safely call this method from any thread of your app.

## See Also

### Finder File Labels
- [var fileLabels: [String]](./filelabels.md)
  The array of file labels, returned as strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/filelabelcolors)*