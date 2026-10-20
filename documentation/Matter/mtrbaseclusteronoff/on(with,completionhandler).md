# on(with:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use onWithParams:completion:

## Declaration

```swift
func on(with params: MTROnOffClusterOnParams?, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func on(with params: MTROnOffClusterOnParams?) async throws
```

```objc
- (void) onWithParams:(MTROnOffClusterOnParams *) params completionHandler:(MTRStatusCompletion) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteronoff/on(with:completionhandler:))*