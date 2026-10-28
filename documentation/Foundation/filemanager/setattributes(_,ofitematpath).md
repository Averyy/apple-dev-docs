# setAttributes(_:ofItemAtPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the attributes of the specified file or directory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setAttributes(_ attributes: [FileAttributeKey : Any], ofItemAtPath path: String) throws
```

```objc
- (BOOL) setAttributes:(NSDictionary<NSString *,id> *) attributes ofItemAtPath:(NSString *) path error:(NSError **) error;
```

## Discussion

As in the POSIX standard, the app either must own the file or directory or must be running as superuser for attribute changes to take effect. The method attempts to make all changes specified in attributes and ignores any rejection of an attempted modification. If the last component of the path is a symbolic link, the system traverses it.

You must initialize the [`posixPermissions`](../fileattributekey/posixpermissions.md) value with the code representing the POSIX file-permissions bit pattern. The system sets [`hfsCreatorCode`](../fileattributekey/hfscreatorcode.md) and [`hfsTypeCode`](../fileattributekey/hfstypecode.md) only when `path` specifies a file.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `attributes`: A dictionary containing as keys the attributes to set for `path` and as values the corresponding value for the attribute. You can set the following attributes: [`busy`](../fileattributekey/busy.md), [`creationDate`](../fileattributekey/creationdate.md), [`extensionHidden`](../fileattributekey/extensionhidden.md), [`groupOwnerAccountID`](../fileattributekey/groupowneraccountid.md), [`groupOwnerAccountName`](../fileattributekey/groupowneraccountname.md), [`hfsCreatorCode`](../fileattributekey/hfscreatorcode.md), [`hfsTypeCode`](../fileattributekey/hfstypecode.md), [`immutable`](../fileattributekey/immutable.md), [`modificationDate`](../fileattributekey/modificationdate.md), [`ownerAccountID`](../fileattributekey/owneraccountid.md), [`ownerAccountName`](../fileattributekey/owneraccountname.md), [`posixPermissions`](../fileattributekey/posixpermissions.md). You can change single attributes or any combination of attributes; you need not specify keys for all attributes.
- `path`: The path of a file or directory.

## See Also

### Getting and setting attributes
- [func componentsToDisplay(forPath: String) -> [String]?](./componentstodisplay%28forpath%29.md)
  Returns an array of strings representing the user-visible components of a given path.
- [func displayName(atPath: String) -> String](./displayname%28atpath%29.md)
  Returns the display name of the file or directory at a specified path.
- [func attributesOfItem(atPath: String) throws -> [FileAttributeKey : Any]](./attributesofitem%28atpath%29.md)
  Returns the attributes of the item at a given path.
- [func attributesOfFileSystem(forPath: String) throws -> [FileAttributeKey : Any]](./attributesoffilesystem%28forpath%29.md)
  Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/setattributes(_:ofitematpath:))*