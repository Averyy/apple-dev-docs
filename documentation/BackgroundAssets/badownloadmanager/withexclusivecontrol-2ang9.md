# withExclusiveControl(_:)

**Framework**: Background Assets  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func withExclusiveControl(_ performHandler: @escaping (Bool, (any Error)?) -> Void)
```

#### Discussion

Acquires exclusive access to the BADownloadManager across the app and application extension.

Acquires exclusive access to the BADownloadManager across the app and application extension. This ensures that your extension and app do not perform operations at the same time. Both the extension and app must use this API to ensure exclusive access.

## Parameters

- `performHandler`: A block that will be executed once exclusive control is acquired. If an error is non-nil then a problem occurred acquiring exclusive access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(_:)-2ang9)*