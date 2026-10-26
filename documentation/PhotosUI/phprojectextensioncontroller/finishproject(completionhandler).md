# finishProject(completionHandler:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func finishProject(completionHandler completion: @escaping @Sendable () -> Void)
```

```swift
func finishProject() async
```

```objc
- (void) finishProjectWithCompletionHandler:(void (^)()) completion;
```

## Parameters

- `completion`: A completion handler to execute before exiting the extension.

## See Also

### Tracking the Project Extension Life Cycle
- [func beginProject(with: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: ((any Error)?) -> Void)](./beginproject%28with,projectinfo,completion%29.md)
  Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [func resumeProject(with: PHProjectExtensionContext, completion: ((any Error)?) -> Void)](./resumeproject%28with,completion%29.md)
  Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.
- [func typeDescriptionDataSource(for: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource](./typedescriptiondatasource%28for,invalidator%29.md)
  Fetches the type description data source to provide the user with more information about the project extension category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller/finishproject(completionhandler:))*