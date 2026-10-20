# stopApp(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func stopApp(with params: MTRApplicationLauncherClusterStopAppParams?, completion: @escaping @Sendable (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)
```

```swift
func stopApp(with params: MTRApplicationLauncherClusterStopAppParams?) async throws -> MTRApplicationLauncherClusterLauncherResponseParams
```

```objc
- (void) stopAppWithParams:(MTRApplicationLauncherClusterStopAppParams *) params completion:(void (^)(MTRApplicationLauncherClusterLauncherResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationlauncher/stopapp(with:completion:))*