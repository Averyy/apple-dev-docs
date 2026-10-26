# beginProject(with:projectInfo:completion:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an opportunity to customize the initial state when the user creates a project using the extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func beginProject(with extensionContext: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func beginProject(with extensionContext: PHProjectExtensionContext, projectInfo: PHProjectInfo) async throws
```

```objc
- (void) beginProjectWithExtensionContext:(PHProjectExtensionContext *) extensionContext projectInfo:(PHProjectInfo *) projectInfo completion:(void (^)(NSError *)) completion;
```

## Parameters

- `extensionContext`: The extension context with access to the project assets.
- `projectInfo`: Information about the project the extension is called on.
- `completion`: A closure with code you provide that runs on completion.

## See Also

### Tracking the Project Extension Life Cycle
- [func finishProject(completionHandler: () -> Void)](./finishproject%28completionhandler%29.md)
  Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [func resumeProject(with: PHProjectExtensionContext, completion: ((any Error)?) -> Void)](./resumeproject%28with,completion%29.md)
  Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.
- [func typeDescriptionDataSource(for: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource](./typedescriptiondatasource%28for,invalidator%29.md)
  Fetches the type description data source to provide the user with more information about the project extension category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/beginproject(with:projectinfo:completion:))*