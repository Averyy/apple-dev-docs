# localizedDescription(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the localized description for the specified Uniform Type Identifier (UTI).

**Availability**:
- macOS 10.5+

## Declaration

```swift
func localizedDescription(forType typeName: String) -> String?
```

#### Return Value

An [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) containing the localized description of `typeName`. You may display this string to the user.

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `typeName`: A string containing the UTI.

## See Also

- [func type(ofFile: String) throws -> String](nsworkspace/type(offile:).md)
  Returns the uniform type identifier of the specified file, if it can be determined.
- [func preferredFilenameExtension(forType: String) -> String?](nsworkspace/preferredfilenameextension(fortype:).md)
  Returns the preferred filename extension for the specified Uniform Type Identifier (UTI).
- [func filenameExtension(String, isValidForType: String) -> Bool](nsworkspace/filenameextension(_:isvalidfortype:).md)
  Returns whether the specified filename extension is appropriate for the Uniform Type Identifier (UTI).
- [func type(String, conformsToType: String) -> Bool](nsworkspace/type(_:conformstotype:).md)
  Returns a Boolean indicating that the first Uniform Type Identifier (UTI) conforms to the second UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/localizeddescription(fortype:))*