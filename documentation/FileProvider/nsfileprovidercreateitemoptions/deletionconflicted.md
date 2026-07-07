# deletionConflicted

**Framework**: File Provider  
**Kind**: property

A value indicating a conflict for a deleted item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
static var deletionConflicted: NSFileProviderCreateItemOptions { get }
```

#### Discussion

If the File Provider extension signals the deletion of an item but the deletion conflicts with local edits, the system attempts to create the modified item by calling the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) method, and passing this value as an option.

## See Also

- [static var mayAlreadyExist: NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions/mayalreadyexist.md)
  An option indicating that the item may already exist in your remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercreateitemoptions/deletionconflicted)*