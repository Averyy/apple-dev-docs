# NSFileProviderModifyItemOptions

**Framework**: File Provider  
**Kind**: struct

Options for modifying items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderModifyItemOptions
```

## Topics

### Choosing Modify Item Options
- [static var mayAlreadyExist: NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions/mayalreadyexist.md)
  An option indicating that the changes may already exist in your remote storage.
### Creating Modify Options
- [init(rawValue: UInt)](nsfileprovidermodifyitemoptions/init(rawvalue:).md)
  Creates an option instance from the raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func createItem(basedOn: NSFileProviderItem, fields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderCreateItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md)
  Tells the file provider to create or import an item based on a template.
- [struct NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md)
  Tells the file provider that an item’s content or metadata changed.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:).md)
  Tells the file provider to delete an item forever.
- [struct NSFileProviderDeleteItemOptions](nsfileproviderdeleteitemoptions.md)
  Options for deleting items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions)*