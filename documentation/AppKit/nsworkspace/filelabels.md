# fileLabels

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of file labels, returned as strings.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var fileLabels: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * fileLabels;
```

#### Return Value

An array of strings.

#### Discussion

You can listen for notifications named [`didChangeFileLabelsNotification`](./didchangefilelabelsnotification.md) to be notified when file labels change.

You can safely call this method from any thread of your app.

## See Also

### Finder File Labels
- [var fileLabelColors: [NSColor]](./filelabelcolors.md)
  The array of colors for the file labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/filelabels)*