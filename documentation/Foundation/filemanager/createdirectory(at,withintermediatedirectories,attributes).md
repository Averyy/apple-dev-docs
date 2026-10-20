# createDirectory(at:withIntermediateDirectories:attributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a directory with the given attributes at the specified URL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func createDirectory(at url: URL, withIntermediateDirectories createIntermediates: Bool, attributes: [FileAttributeKey : Any]? = nil) throws
```

```objc
- (BOOL) createDirectoryAtURL:(NSURL *) url withIntermediateDirectories:(BOOL) createIntermediates attributes:(NSDictionary<NSString *,id> *) attributes error:(NSError **) error;
```

#### Discussion

If you specify `nil` for the `attributes` parameter, this method uses a default set of values for the owner, group, and permissions of any newly created directories in the path. Similarly, if you omit a specific attribute, the default value is used. The default values for newly created directories are as follows:

- Permissions are set according to the umask of the current process. For more information, see umask.
- The owner ID is set to the effective user ID of the process.
- The group ID is set to that of the parent directory.

If you want to specify a relative path for url, you must set the current working directory before creating the corresponding [`NSURL`](../nsurl.md) object.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: A file URL that specifies the directory to create. If you want to specify a relative path, you must set the current working directory before creating the corresponding [`NSURL`](../nsurl.md) object. This parameter must not be `nil`.
- `createIntermediates`: If [`true`](../../Swift/true.md), this method creates any nonexistent parent directories as part of creating the directory in `url`. If [`false`](../../Swift/false.md), this method fails if any of the intermediate parent directories does not exist.
- `attributes`: The file attributes for the new directory. You can set the owner and group numbers, file permissions, and modification date. If you specify `nil` for this parameter, the directory is created according to the umask(2) macOS Developer Tools Manual Page of the process. The Supporting Types section lists the global constants used as keys in the `attributes` dictionary. Some of the keys, such as [`hfsCreatorCode`](../fileattributekey/hfscreatorcode.md) and [`hfsTypeCode`](../fileattributekey/hfstypecode.md), do not apply to directories.

## See Also

### Related Documentation
- [func setAttributes([FileAttributeKey : Any], ofItemAtPath: String) throws](./setattributes%28_,ofitematpath%29.md)
  Sets the attributes of the specified file or directory.
### Creating and deleting items
- [func createDirectory(atPath: String, withIntermediateDirectories: Bool, attributes: [FileAttributeKey : Any]?) throws](./createdirectory%28atpath,withintermediatedirectories,attributes%29.md)
  Creates a directory with given attributes at the specified path.
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](./createfile%28atpath,contents,attributes%29.md)
  Creates a file with the specified content and attributes at the given location.
- [func removeItem(at: URL) throws](./removeitem%28at%29.md)
  Removes the file or directory at the specified URL.
- [func removeItem(atPath: String) throws](./removeitem%28atpath%29.md)
  Removes the file or directory at the specified path.
- [func trashItem(at: URL, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](./trashitem%28at,resultingitemurl%29.md)
  Moves an item to the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/createdirectory(at:withintermediatedirectories:attributes:))*