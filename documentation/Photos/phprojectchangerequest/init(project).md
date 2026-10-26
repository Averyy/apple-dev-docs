# init(project:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a change request around the specified project.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init(project: PHProject)
```

```objc
- (instancetype) initWithProject:(PHProject *) project;
```

## Parameters

- `project`: The project being changed in the request.

## See Also

### Creating Change Requests
- [var title: String](./title.md)
  The title of the change request.
- [var projectExtensionData: Data](./projectextensiondata.md)
  Compressed project-specific data to use in the change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest/init(project:))*