# typeDescriptionDataSource(for:invalidator:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Fetches the type description data source to provide the user with more information about the project extension category.

**Availability**:
- macOS 10.14+

## Declaration

```swift
optional func typeDescriptionDataSource(for category: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource
```

```objc
- (id<PHProjectTypeDescriptionDataSource>) typeDescriptionDataSourceForCategory:(PHProjectCategory) category invalidator:(id<PHProjectTypeDescriptionInvalidator>) invalidator;
```

#### Discussion

Extensions can define any number of project types to support. The types appear to users as choices in the Photos app upon initial project creation. To enable this entry point into the extension, include the key/value pair `PHProjectExtensionDefinesProjectTypes`: `YES` in the Xcode project’s `Info.plist` file. Once enabled, Photos asks your extension for its list of supported project types. The option the user selects is passed to the extension as an attribute of [`PHProjectInfo`](../phprojectinfo.md).

## Parameters

- `category`: The category in which the user selected the extension.
- `invalidator`: An object used to invalidate information returned from the data source.

## See Also

### Tracking the Project Extension Life Cycle
- [func beginProject(with: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: ((any Error)?) -> Void)](./beginproject%28with,projectinfo,completion%29.md)
  Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [func finishProject(completionHandler: () -> Void)](./finishproject%28completionhandler%29.md)
  Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [func resumeProject(with: PHProjectExtensionContext, completion: ((any Error)?) -> Void)](./resumeproject%28with,completion%29.md)
  Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/typedescriptiondatasource(for:invalidator:))*