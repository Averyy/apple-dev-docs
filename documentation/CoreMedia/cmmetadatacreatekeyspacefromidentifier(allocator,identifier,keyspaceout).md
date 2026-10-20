# CMMetadataCreateKeySpaceFromIdentifier(allocator:identifier:keySpaceOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a copy of the keyspace by using an identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMMetadataCreateKeySpaceFromIdentifier(allocator: CFAllocator?, identifier: CFString, keySpaceOut: UnsafeMutablePointer<CFString?>) -> OSStatus
```

```c
extern OSStatus CMMetadataCreateKeySpaceFromIdentifier(CFAllocatorRef allocator, CFStringRef identifier, CFStringRef*keySpaceOut);
```

#### Return Value

If successful, a nonzero result code. See [Metadata Identifier Error Codes](./metadata-identifier-errors.md).

## Parameters

- `allocator`: The allocator to use for creating the identifier.
- `identifier`: The identifier to be inspected.
- `keySpaceOut`: Upon return, a pointer to the keyspace that was used to create the identifier.

## See Also

### Creating Metadata Identifiers
- [func CMMetadataCreateIdentifierForKeyAndKeySpace(allocator: CFAllocator?, key: CFTypeRef, keySpace: CFString, identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus](./cmmetadatacreateidentifierforkeyandkeyspace%28allocator,key,keyspace,identifierout%29.md)
  Creates a URL-like string identifier that represents a key or keyspace tuple.
- [func CMMetadataCreateKeyFromIdentifier(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus](./cmmetadatacreatekeyfromidentifier%28allocator,identifier,keyout%29.md)
  Creates a copy of the key by using an identifier.
- [func CMMetadataCreateKeyFromIdentifierAsCFData(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFData?>) -> OSStatus](./cmmetadatacreatekeyfromidentifierascfdata%28allocator,identifier,keyout%29.md)
  Creates a copy of the key by using an identifier, and results in a core foundation data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatacreatekeyspacefromidentifier(allocator:identifier:keyspaceout:))*