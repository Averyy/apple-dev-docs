# launchContent(with:completion:)

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
func launchContent(with params: MTRContentLauncherClusterLaunchContentParams, completion: @escaping @Sendable (MTRContentLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)
```

```swift
func launchContent(with params: MTRContentLauncherClusterLaunchContentParams) async throws -> MTRContentLauncherClusterLauncherResponseParams
```

```objc
- (void) launchContentWithParams:(MTRContentLauncherClusterLaunchContentParams *) params completion:(void (^)(MTRContentLauncherClusterLauncherResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercontentlauncher/launchcontent(with:completion:))*