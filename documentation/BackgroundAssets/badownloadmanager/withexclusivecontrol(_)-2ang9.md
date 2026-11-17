# withExclusiveControl(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire immediate, exclusive access to the download manager.

**Availability**:
- iOS 16.1+ - Deprecated in 27.0
- iPadOS 16.1+ - Deprecated in 27.0
- Mac Catalyst 16.1+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.0
- tvOS 18.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

> **Deprecated**: Use the asynchronous overload of withExclusiveControl(_:) instead.

## Declaration

```swift
func withExclusiveControl(_ performHandler: @escaping (Bool, (any Error)?) -> Void)
```

```objc
- (void) performWithExclusiveControl:(void (^)(BOOL acquiredLock, NSError *error)) performHandler;
```

## Discussion

The handler takes the following parameter:

- An error if a problems occurs, or `nil` if the method successfully acquires exclusive access.

To prevent race conditions, always acquire exclusive control of the download manager before you schedule new assets downloads, or fetch or cancel existing downloads. Because the handler yields control as soon as it returns, complete all work that depends on exclusivity in the handler’s body.

```swift
let manager = BADownloadManager.shared

// Attempt to acquire exclusive access of the download manager.
manager.withExclusiveControl { error in
    // Return immediately if the attempt fails.
    if let error {
        print(error.localizedDescription)
        return
    }
    
    // Perform the work that requires exclusive access.
    // Return and yield control to the system.
}
```

## Parameters

- `performHandler`: The handler that performs the work requiring exclusive access to the download manager, which the system executes on an arbitrary queue.

## See Also

### Synchronizing manager access
- [func withExclusiveControl(beforeDate: Date, perform: (Bool, (any Error)?) -> Void)](./withexclusivecontrol%28beforedate,perform%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(_:)-2ang9)*