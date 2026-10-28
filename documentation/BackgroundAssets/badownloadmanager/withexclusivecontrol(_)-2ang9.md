# withExclusiveControl(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

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

Acquires exclusive access to the BADownloadManager across the app and application extension.

Acquires exclusive access to the BADownloadManager across the app and application extension. This ensures that your extension and app do not perform operations at the same time. Both the extension and app must use this API to ensure exclusive access.

## Parameters

- `performHandler`: A block that will be executed once exclusive control is acquired. If an error is non-nil then a problem occurred acquiring exclusive access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(_:)-2ang9)*