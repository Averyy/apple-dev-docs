# withExclusiveControl(_:)

**Framework**: Background Assets  
**Kind**: method

Attempts to acquire immediate, exclusive control over the download manager.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@backDeployed(before: iOS 27, macOS 27, tvOS 27, visionOS 27)
final func withExclusiveControl<ReturnType>(_ body: @escaping () throws -> sending ReturnType) async throws -> sending ReturnType
```

#### Return Value

`body`’s return value.

#### Discussion

To avoid races between your main app and your downloader extension, perform operations on the download manager—*e.g.*, fetching current downloads, scheduling new downloads, *etc.*—while maintaining exclusive control over it. Unlike [`withExclusiveControl(_:)`](badownloadmanager/withexclusivecontrol(_:)-2ang9.md), this method waits for exclusive control to be acquired and then relinquished before it returns.

> **Note**: When `body` throws or when exclusive control over the download manager can’t be acquired.

## Parameters

- `body`: A closure to execute with exclusive control over the download manager. Once the closure returns or throws, you lose exclusive control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(_:)-1rf9w)*