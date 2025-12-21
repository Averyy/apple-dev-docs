# specializedName

**Framework**: Metal  
**Kind**: property

A new name for the created function object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var specializedName: String? { get set }
```

#### Discussion

The default value is `nil`. If you specify a value for this property, Metal creates the new [`MTLFunction`](mtlfunction.md) object with the new name. Use this property if you want to specialize a function with multiple variants and give each a distinct name.

## See Also

- [var name: String?](mtlfunctiondescriptor/name.md)
  The name of the function to fetch from the library.
- [var constantValues: MTLFunctionConstantValues?](mtlfunctiondescriptor/constantvalues.md)
  The set of constant values assigned to the function constants.
- [var options: MTLFunctionOptions](mtlfunctiondescriptor/options.md)
  Flags specifying how Metal should create the new function object.
- [var binaryArchives: [any MTLBinaryArchive]?](mtlfunctiondescriptor/binaryarchives.md)
  The binary archives to search for a previously-compiled version of this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.
- [class MTLLinkedFunctions](mtllinkedfunctions.md)
  A set of related functions that Metal links to when necessary to create the function instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/specializedname)*