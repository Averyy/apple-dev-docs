# loadAllManagersFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Asynchronously reads all the relay configurations previously created and saved by the calling app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func loadAllManagersFromPreferences(completionHandler: @escaping @Sendable ([NERelayManager], (any Error)?) -> Void)
```

```swift
class func loadAllManagersFromPreferences() async throws -> [NERelayManager]
```

```objc
+ (void) loadAllManagersFromPreferencesWithCompletionHandler:(void (^)(NSArray<NERelayManager *> *managers, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block that receives an array of [`NERelayManager`](../nerelaymanager.md) objects. If the system failed to read any [`NERelay`](../nerelay.md) configurations read from the disk, the array is passes to the block is empty. The [`NSError`](../../Foundation/nserror.md) passed to this block is `nil` if the load operation succeeded, non-`nil` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/loadallmanagersfrompreferences(completionhandler:))*