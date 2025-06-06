# name

**Framework**: Metal  
**Kind**: property

The name of the function to fetch from the library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var name: String? { get set }
```

## See Also

- [var specializedName: String?](mtlfunctiondescriptor/specializedname.md)
  A new name for the created function object.
- [var constantValues: MTLFunctionConstantValues?](mtlfunctiondescriptor/constantvalues.md)
  The set of constant values assigned to the function constants.
- [var options: MTLFunctionOptions](mtlfunctiondescriptor/options.md)
  Flags specifying how Metal should create the new function object.
- [var binaryArchives: [any MTLBinaryArchive]?](mtlfunctiondescriptor/binaryarchives.md)
  The binary archives to search for a previously-compiled version of this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal creates the function object.
- [class MTLLinkedFunctions](mtllinkedfunctions.md)
  A set of related functions that Metal links to when necessary to create the function object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/name)*