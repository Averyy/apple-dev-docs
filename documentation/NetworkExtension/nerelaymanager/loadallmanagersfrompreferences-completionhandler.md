# loadAllManagersFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

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
class func loadAllManagersFromPreferences() async throws -> [NERelayManager]
```

## Parameters

- `completionHandler`: A block that receives an array of   objects. If the system failed to read any   configurations read from the disk, the array is passes to the block is empty. The   passed to this block is   if the load operation succeeded, non-  otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/loadallmanagersfrompreferences(completionhandler:))*