# resumeProject(with:completion:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func resumeProject(with extensionContext: PHProjectExtensionContext, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func resumeProject(with extensionContext: PHProjectExtensionContext) async throws
```

```objc
- (void) resumeProjectWithExtensionContext:(PHProjectExtensionContext *) extensionContext completion:(void (^)(NSError *)) completion;
```

## Parameters

- `extensionContext`: The extension context with access to the project assets.
- `completion`: A completion handler to execute upon returning to the extension.

## See Also

### Tracking the Project Extension Life Cycle
- [func beginProject(with: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: ((any Error)?) -> Void)](./beginproject%28with,projectinfo,completion%29.md)
  Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [func finishProject(completionHandler: () -> Void)](./finishproject%28completionhandler%29.md)
  Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [func typeDescriptionDataSource(for: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource](./typedescriptiondatasource%28for,invalidator%29.md)
  Fetches the type description data source to provide the user with more information about the project extension category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/resumeproject(with:completion:))*