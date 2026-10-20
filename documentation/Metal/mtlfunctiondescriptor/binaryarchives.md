# binaryArchives

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The binary archives to search for a previously-compiled version of this function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<id<MTLBinaryArchive>> * binaryArchives;
```

## Mentions

- [Compiling binary archives from a custom configuration script](../compiling-binary-archives-from-a-custom-configuration-script.md)

#### Discussion

If you specify an archive that includes a fully compiled version of this function, Metal uses the compiled version rather than creating a new one.

## See Also

### Specifying the function configuration
- [var name: String?](./name.md)
  The name of the function to fetch from the library.
- [var specializedName: String?](./specializedname.md)
  A new name for the created function object.
- [var constantValues: MTLFunctionConstantValues?](./constantvalues.md)
  The set of constant values assigned to the function constants.
- [var options: MTLFunctionOptions](./options.md)
  Flags specifying how Metal should create the new function object.
- [struct MTLFunctionOptions](../mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.
- [class MTLLinkedFunctions](../mtllinkedfunctions.md)
  A set of related functions that Metal links to when necessary to create the function instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/binaryarchives)*