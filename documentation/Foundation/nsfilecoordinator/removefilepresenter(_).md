# removeFilePresenter(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) removeFilePresenter:(id<NSFilePresenter>) filePresenter;
```

## Discussion

Call this method to unregister file presenters before those objects are deallocated, even in a garbage-collected application.

## Parameters

- `filePresenter`: The file presenter object to unregister. If the object is not currently registered, this method does nothing.

## See Also

### Managing File Presenters
- [class func addFilePresenter(any NSFilePresenter)](./addfilepresenter%28_%29.md)
  Registers the specified file presenter object so that it can receive notifications.
- [class var filePresenters: [any NSFilePresenter]](./filepresenters.md)
  Returns an array containing the currently registered file presenter objects.
- [var purposeIdentifier: String](./purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/removefilepresenter(_:))*