# filePresenters

**Framework**: Foundation  
**Kind**: property

Returns an array containing the currently registered file presenter objects.

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
class var filePresenters: [any NSFilePresenter] { get }
```

#### Return Value

An array of objects that conform to the [`NSFilePresenter`](nsfilepresenter.md) protocol.

## See Also

- [class func addFilePresenter(any NSFilePresenter)](nsfilecoordinator/addfilepresenter(_:).md)
  Registers the specified file presenter object so that it can receive notifications.
- [class func removeFilePresenter(any NSFilePresenter)](nsfilecoordinator/removefilepresenter(_:).md)
  Unregisters the specified file presenter object.
- [var purposeIdentifier: String](nsfilecoordinator/purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/filepresenters)*