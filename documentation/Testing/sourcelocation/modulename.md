# moduleName

**Framework**: Swift Testing  
**Kind**: property

The name of the module containing the source file.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
var moduleName: String { get }
```

#### Discussion

The name of the module is derived from this instance’s [`fileID`](sourcelocation/fileid.md) property. It consists of the substring of the file ID up to the first forward-slash character (`"/"`.) For example, if the value of this instance’s [`fileID`](sourcelocation/fileid.md) property is `"FoodTruck/WheelTests.swift"`, the module name is `"FoodTruck"`.

The structure of file IDs is described in the documentation for the [`#fileID`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/fileID()) macro in the Swift standard library.

## See Also

- [var fileID: String](sourcelocation/fileid.md)
  The file ID of the source file.
- [var fileName: String](sourcelocation/filename.md)
  The name of the source file.
- [#fileID](https://developer.apple.comhttps://developer.apple.com/documentation/swift/fileID())


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/sourcelocation/modulename)*