# PHProjectChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A request to change asset data in a Photos project extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectChangeRequest
```

```objc
@interface PHProjectChangeRequest : PHChangeRequest
```

#### Overview

Make a project change request to alter a project’s title or metadata. Respond to project change requests by updating your user interface as assets are added, modified, or removed.

## Topics

### Creating Change Requests
- [init(project: PHProject)](./phprojectchangerequest/init%28project%29.md)
  Creates a change request around the specified project.
- [var title: String](./phprojectchangerequest/title.md)
  The title of the change request.
- [var projectExtensionData: Data](./phprojectchangerequest/projectextensiondata.md)
  Compressed project-specific data to use in the change request.
### Responding to Change Requests
- [func setProjectPreviewImage(NSImage)](./phprojectchangerequest/setprojectpreviewimage%28_%29.md)
  Updates the project preview in Photos.
- [func setKeyAsset(PHAsset?)](./phprojectchangerequest/setkeyasset%28_%29.md)
  Sets the key asset representing the project.
### Removing Assets
- [func removeAssets<T>(T)](./phprojectchangerequest/removeassets%28_%29-n825.md)
  Removes assets of a certain type from the collection.
- [func removeAssets(PHFetchResult<PHAsset>)](./phprojectchangerequest/removeassets%28_%29-3ytt3.md)
  Removes assets based on a fetch result.

## Relationships

### Inherits From
- [PHChangeRequest](./phchangerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class PHProject](./phproject.md)
  A representation of a Photos app project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest)*