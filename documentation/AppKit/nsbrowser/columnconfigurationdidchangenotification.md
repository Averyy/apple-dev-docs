# columnConfigurationDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Notifies the delegate when the width of a browser column has changed.

**Availability**:
- macOS

## Declaration

```swift
class let columnConfigurationDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSBrowserColumnConfigurationDidChangeNotification;
```

## Discussion

The notification object is the browser whose column sizes need to be made persistent. This notification does not contain a `userInfo` dictionary. If the user resizes more than one column, a single notification is posted when the user is finished resizing.

## See Also

### Related Documentation
- [func browserColumnConfigurationDidChange(Notification)](../nsbrowserdelegate/browsercolumnconfigurationdidchange%28_%29.md)
  Used by clients to implement their own column width persistence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/columnconfigurationdidchangenotification)*