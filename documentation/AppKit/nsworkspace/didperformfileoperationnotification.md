# didPerformFileOperationNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when a file operation has been performed in the receiving app.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
class let didPerformFileOperationNotification: NSNotification.Name
```

```c
extern NSNotificationName NSWorkspaceDidPerformFileOperationNotification;
```

## Discussion

The notification object is the shared `NSWorkspace` instance. The `userInfo` dictionary contains a key `@"NSOperationNumber"` with a `NSNumber` object containing an integer indicating the type of file operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/didperformfileoperationnotification)*