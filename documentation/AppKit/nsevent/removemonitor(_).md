# removeMonitor(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Removes the specified event monitor.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func removeMonitor(_ eventMonitor: Any)
```

```objc
+ (void) removeMonitor:(id) eventMonitor;
```

## Discussion

You must ensure that `eventMonitor` is removed only once. Removing the same `eventMonitor` instance multiple times results in an over-release condition, even in a Garbage Collected environment

## Parameters

- `eventMonitor`: The event handler object to remove.

## See Also

### Monitoring app events
- [class func addGlobalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> Void) -> Any?](./addglobalmonitorforevents%28matching,handler%29.md)
  Installs an event monitor that receives copies of events the system posts to other applications.
- [class func addLocalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> NSEvent?) -> Any?](./addlocalmonitorforevents%28matching,handler%29.md)
  Installs an event monitor that receives copies of events the system posts to this app prior to their dispatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/removemonitor(_:))*