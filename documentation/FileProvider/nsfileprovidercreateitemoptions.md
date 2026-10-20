# NSFileProviderCreateItemOptions

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Options for creating items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderCreateItemOptions
```

```c
enum NSFileProviderCreateItemOptions : NSUInteger;
```

## Topics

### Choosing Create Item Options
- [static var mayAlreadyExist: NSFileProviderCreateItemOptions](./nsfileprovidercreateitemoptions/mayalreadyexist.md)
  An option indicating that the item may already exist in your remote storage.
- [static var deletionConflicted: NSFileProviderCreateItemOptions](./nsfileprovidercreateitemoptions/deletionconflicted.md)
  A value indicating a conflict for a deleted item.
### Creating Options
- [init(rawValue: UInt)](./nsfileprovidercreateitemoptions/init%28rawvalue%29.md)
  Creates an option instance from the raw value.

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
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md)
  Tells the file provider that an item’s content or metadata changed.
- [struct NSFileProviderModifyItemOptions](./nsfileprovidermodifyitemoptions.md)
  Options for modifying items.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/deleteitem%28identifier,baseversion,options,request,completionhandler%29.md)
  Tells the file provider to delete an item forever.
- [struct NSFileProviderDeleteItemOptions](./nsfileproviderdeleteitemoptions.md)
  Options for deleting items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercreateitemoptions)*