# deleteAllData()

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

Removes all persisted model data from the app’s persistent storage.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2 (renamed: erase)
- iPadOS 17.0+ - Deprecated in 27.2 (renamed: erase)
- Mac Catalyst 17.0+ - Deprecated in 27.2 (renamed: erase)
- macOS 14.0+ - Deprecated in 27.2 (renamed: erase)
- tvOS 17.0+ - Deprecated in 27.2 (renamed: erase)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: erase)
- watchOS 10.0+ - Deprecated in 27.2 (renamed: erase)
- Swift 5.9+

> **Deprecated**: deleteAllData has been replaced by `erase`. Use `erase` to completely remove all of the data from a store.

## Declaration

```swift
func deleteAllData()
```

#### Discussion

> ⚠️ **Warning**: After you call this method, the container immediately deletes all data from the app’s persistent storage. This deletion is permanent and cannot be undone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/deletealldata())*