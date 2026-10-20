# launchApp(with:completion:)

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
func launchApp(with params: MTRApplicationLauncherClusterLaunchAppParams?, completion: @escaping @Sendable (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)
```

```swift
func launchApp(with params: MTRApplicationLauncherClusterLaunchAppParams?) async throws -> MTRApplicationLauncherClusterLauncherResponseParams
```

```objc
- (void) launchAppWithParams:(MTRApplicationLauncherClusterLaunchAppParams *) params completion:(void (^)(MTRApplicationLauncherClusterLauncherResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationlauncher/launchapp(with:completion:))*