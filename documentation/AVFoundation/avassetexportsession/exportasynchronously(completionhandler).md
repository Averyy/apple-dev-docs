# exportAsynchronously(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Starts the asynchronous execution of an export session.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0
- iPadOS 4.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`export(to:as:isolation:)`](./export%28to,as,isolation%29.md) instead.

## Declaration

```swift
func exportAsynchronously(completionHandler handler: @escaping @Sendable () -> Void)
```

```swift
func export() async
```

```objc
- (void) exportAsynchronouslyWithCompletionHandler:(void (^)()) handler;
```

## Parameters

- `handler`: A callback the system invokes when it finishes successfully, or in the event of writing failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportasynchronously(completionhandler:))*