# colorDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](nscolorpanel.md) is invoked.

**Availability**:
- macOS ?+

## Declaration

```swift
class let colorDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the notifying `NSColorPanel`. This notification does not contain a `userInfo` dictionary.

## See Also

- [protocol NSColorChanging](nscolorchanging.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/colordidchangenotification)*