# allowedTypes

**Framework**: AppKit  
**Kind**: property

Sets the component types allowed in the path when the cell is editable.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var allowedTypes: [String]? { get set }
```

#### Discussion

The `allowedTypes` array can contain file extensions (without the period that begins the extension) or UTIs. To allow folders, include the `public.folder` identifier. To allow any type, use `nil`. If the value of `allowedTypes` is an empty array, nothing is allowed. The default value is `nil`, allowing all types.

If the cell is editable and its type is `NSPathStylePopUp`, a Choose item is included to enable selection of a different path by invoking an Open panel. The allowed types are passed to the Open panel to filter out other types. The allowed types are also used with drag and drop to indicate if a drop is allowed.

## Parameters

- `allowedTypes`: An array of strings representing either file extensions or UTIs. Can be  , the default value, allowing all types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/allowedtypes)*