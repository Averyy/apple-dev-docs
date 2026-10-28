# deletionConflicted

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A value indicating a conflict for a deleted item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
static var deletionConflicted: NSFileProviderCreateItemOptions { get }
```

```c
NSFileProviderCreateItemDeletionConflicted
```

## Discussion

If the File Provider extension signals the deletion of an item but the deletion conflicts with local edits, the system attempts to create the modified item by calling the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md) method, and passing this value as an option.

## See Also

### Choosing Create Item Options
- [static var mayAlreadyExist: NSFileProviderCreateItemOptions](./mayalreadyexist.md)
  An option indicating that the item may already exist in your remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercreateitemoptions/deletionconflicted)*