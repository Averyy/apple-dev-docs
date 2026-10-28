# supportedProjectTypes

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of project types the extension supports.

**Availability**:
- macOS 10.13+ - Deprecated in 10.14

## Declaration

```swift
optional var supportedProjectTypes: [PHProjectTypeDescription] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PHProjectTypeDescription *> * supportedProjectTypes;
```

## Discussion

Extensions can define any number of project types to support. The types appear to users as choices in the Photos app upon initial project creation. To enable this e ntry point into the extension, include the key/value pair `PHProjectExtensionDefinesProjectTypes`: `YES` in the Xcode project’s Info.plist. Once enabled, Photos will ask your extension for its list of supported project types. The option the user selects will be passed to the extension as an attribute of [`PHProjectInfo`](../phprojectinfo.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/supportedprojecttypes)*