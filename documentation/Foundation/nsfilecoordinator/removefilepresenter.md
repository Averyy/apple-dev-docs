# removeFilePresenter(_:)

**Framework**: Foundation  
**Kind**: method

Unregisters the specified file presenter object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func removeFilePresenter(_ filePresenter: any NSFilePresenter)
```

#### Discussion

Call this method to unregister file presenters before those objects are deallocated, even in a garbage-collected application.

## Parameters

- `filePresenter`: The file presenter object to unregister. If the object is not currently registered, this method does nothing.

## See Also

- [class func addFilePresenter(any NSFilePresenter)](nsfilecoordinator/addfilepresenter(_:).md)
  Registers the specified file presenter object so that it can receive notifications.
- [class var filePresenters: [any NSFilePresenter]](nsfilecoordinator/filepresenters.md)
  Returns an array containing the currently registered file presenter objects.
- [var purposeIdentifier: String](nsfilecoordinator/purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/removefilepresenter(_:))*