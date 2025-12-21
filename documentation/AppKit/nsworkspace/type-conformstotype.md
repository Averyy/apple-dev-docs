# type(_:conformsToType:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean indicating that the first Uniform Type Identifier (UTI) conforms to the second UTI.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func type(_ firstTypeName: String, conformsToType secondTypeName: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `firstTypeName` conforms to the UTI hierarchy of `secondTypeName`; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method instead of comparing UTIs for equality. See [`Uniform Type Identifiers Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319) for information about UTI conformance.

This method will always return [`true`](https://developer.apple.com/documentation/Swift/true) if the two strings are equal. Use this method with other type names, including those in the [`CFBundleTypeName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes/CFBundleTypeName) keys of your app’s `Info.plist` file.

You can safely call this method from any thread of your app.

## Parameters

- `firstTypeName`: A string containing the UTI that should conform to  .
- `secondTypeName`: A string containing a UTI.

## See Also

- [func type(ofFile: String) throws -> String](nsworkspace/type(offile:).md)
  Returns the uniform type identifier of the specified file, if it can be determined.
- [func localizedDescription(forType: String) -> String?](nsworkspace/localizeddescription(fortype:).md)
  Returns the localized description for the specified Uniform Type Identifier (UTI).
- [func preferredFilenameExtension(forType: String) -> String?](nsworkspace/preferredfilenameextension(fortype:).md)
  Returns the preferred filename extension for the specified Uniform Type Identifier (UTI).
- [func filenameExtension(String, isValidForType: String) -> Bool](nsworkspace/filenameextension(_:isvalidfortype:).md)
  Returns whether the specified filename extension is appropriate for the Uniform Type Identifier (UTI).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/type(_:conformstotype:))*