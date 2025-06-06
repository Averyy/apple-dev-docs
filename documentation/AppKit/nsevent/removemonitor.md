# removeMonitor(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified event monitor.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func removeMonitor(_ eventMonitor: Any)
```

#### Discussion

You must ensure that `eventMonitor` is removed only once. Removing the same `eventMonitor` instance multiple times results in an over-release condition, even in a Garbage Collected environment

## Parameters

- `eventMonitor`: The event handler object to remove.

## See Also

- [class func addGlobalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> Void) -> Any?](nsevent/addglobalmonitorforevents(matching:handler:).md)
  Installs an event monitor that receives copies of events the system posts to other applications.
- [class func addLocalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> NSEvent?) -> Any?](nsevent/addlocalmonitorforevents(matching:handler:).md)
  Installs an event monitor that receives copies of events the system posts to this app prior to their dispatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/removemonitor(_:))*