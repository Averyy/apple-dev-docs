# purposeIdentifier

**Framework**: Foundation  
**Kind**: property

A string that uniquely identifies the file access that was performed by this file coordinator.

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
var purposeIdentifier: String { get set }
```

#### Discussion

Coordinated reads and writes performed using the same purpose identifier never block each other, even if they occur in different processes. If you are coordinating file access on behalf of a file presenter, use [`init(filePresenter:)`](nsfilecoordinator/init(filepresenter:).md) and do not attempt to set a custom purpose identifier. Every file coordinator instance initialized with the same file presenter has the same purpose identifier.

You may need to set a custom purpose identifier for the following reasons:

- Your application has a File Provider extension. Any file coordination done on behalf of the File Provider needs to be done using the File Provider’s purpose identifier.
- You have two separate subsystems that need to work together to perform a single high-level operation, and both subsystems perform their own coordinated reads or writes. Using the same purpose identifier in both subsystems prevents possible deadlocks between the two subsystems.

When creating custom purpose identifiers, you can use a reverse DNS style string, such as `com.example.MyApplication.MyPurpose`, or a UUID string. You cannot use `nil` or zero-length strings.

> **Note**:  You can set a purpose identifier only once, either implicitly by calling [`init(filePresenter:)`](nsfilecoordinator/init(filepresenter:).md) or explicitly using this property. Attempting to set the purpose identifier a second time throws an exception.

 You can set a purpose identifier only once, either implicitly by calling [`init(filePresenter:)`](nsfilecoordinator/init(filepresenter:).md) or explicitly using this property. Attempting to set the purpose identifier a second time throws an exception.

## See Also

- [class func addFilePresenter(any NSFilePresenter)](nsfilecoordinator/addfilepresenter(_:).md)
  Registers the specified file presenter object so that it can receive notifications.
- [class func removeFilePresenter(any NSFilePresenter)](nsfilecoordinator/removefilepresenter(_:).md)
  Unregisters the specified file presenter object.
- [class var filePresenters: [any NSFilePresenter]](nsfilecoordinator/filepresenters.md)
  Returns an array containing the currently registered file presenter objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/purposeidentifier)*