# filePresenters

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSArray<id<NSFilePresenter>> * filePresenters;
```

## Return Value

An array of objects that conform to the [`NSFilePresenter`](../nsfilepresenter.md) protocol.

## See Also

### Managing File Presenters
- [class func addFilePresenter(any NSFilePresenter)](./addfilepresenter%28_%29.md)
  Registers the specified file presenter object so that it can receive notifications.
- [class func removeFilePresenter(any NSFilePresenter)](./removefilepresenter%28_%29.md)
  Unregisters the specified file presenter object.
- [var purposeIdentifier: String](./purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/filepresenters)*