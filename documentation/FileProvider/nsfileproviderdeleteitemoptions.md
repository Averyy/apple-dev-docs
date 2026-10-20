# NSFileProviderDeleteItemOptions

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Options for deleting items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderDeleteItemOptions
```

```c
enum NSFileProviderDeleteItemOptions : NSUInteger;
```

## Topics

### Choosing Delete Options
- [static var recursive: NSFileProviderDeleteItemOptions](./nsfileproviderdeleteitemoptions/recursive.md)
  A value indicating that the delete operation removes the item and all of its children.
### Creating Delete Options
- [init(rawValue: UInt)](./nsfileproviderdeleteitemoptions/init%28rawvalue%29.md)
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
- [struct NSFileProviderCreateItemOptions](./nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md)
  Tells the file provider that an item’s content or metadata changed.
- [struct NSFileProviderModifyItemOptions](./nsfileprovidermodifyitemoptions.md)
  Options for modifying items.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](./nsfileproviderreplicatedextension/deleteitem%28identifier,baseversion,options,request,completionhandler%29.md)
  Tells the file provider to delete an item forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdeleteitemoptions)*