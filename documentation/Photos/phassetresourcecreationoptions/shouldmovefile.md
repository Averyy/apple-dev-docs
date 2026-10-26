# shouldMoveFile

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether Photos moves or duplicates files when creating an asset resource.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var shouldMoveFile: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL shouldMoveFile;
```

#### Discussion

This property applies only when creating an asset resource with the [`addResource(with:fileURL:options:)`](../phassetcreationrequest/addresource%28with,fileurl,options%29.md) method. If this value is `true`, Photos moves the specified file into the Photos library to create the asset resource, removing the original file after the asset has been successfully created. When using this option, Photos does not make an intermediary copy of the resource data, so no additional storage space is required.

If this value is `false` (the default), Photos copies the contents of the original file into the Photos library.

> **Note**:  Attempting to move a file that is currently open or has hard links fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/shouldmovefile)*