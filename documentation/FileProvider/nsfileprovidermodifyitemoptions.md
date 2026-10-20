# NSFileProviderModifyItemOptions

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Options for modifying items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderModifyItemOptions
```

```c
enum NSFileProviderModifyItemOptions : NSUInteger;
```

## Topics

### Choosing Modify Item Options
- [static var mayAlreadyExist: NSFileProviderModifyItemOptions](./nsfileprovidermodifyitemoptions/mayalreadyexist.md)
  An option that indicates the changes may already exist in your remote storage.
- [static var failOnConflict: NSFileProviderModifyItemOptions](./nsfileprovidermodifyitemoptions/failonconflict.md)
  An option to fail an upload in the event of a version conflict.
### Creating Modify Options
- [init(rawValue: UInt)](./nsfileprovidermodifyitemoptions/init%28rawvalue%29.md)
  Creates an option instance from the raw value.
### Type Properties
- [static var isImmediateUploadRequestByPresentingApplication: NSFileProviderModifyItemOptions](./nsfileprovidermodifyitemoptions/isimmediateuploadrequestbypresentingapplication.md)
  An option to require the upload to complete before calling the completion handler.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing Items
- [func createItem(basedOn: NSFileProviderItem, fields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderCreateItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md)
  Tells the file provider to create or import an item based on a template.
- [struct NSFileProviderCreateItemOptions](./nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md)
  Tells the file provider that an item’s content or metadata changed.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/deleteitem%28identifier,baseversion,options,request,completionhandler%29.md)
  Tells the file provider to delete an item forever.
- [struct NSFileProviderDeleteItemOptions](./nsfileproviderdeleteitemoptions.md)
  Options for deleting items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions)*