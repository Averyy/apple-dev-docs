# CMMetadataCreateKeyFromIdentifierAsCFData(allocator:identifier:keyOut:)

**Framework**: Core Media  
**Kind**: func

Creates a copy of the key by using an identifier, and results in a core foundation data object.

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
func CMMetadataCreateKeyFromIdentifierAsCFData(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

If successful, a nonzero result code. See [`Metadata Identifier Error Codes`](metadata-identifier-errors.md).

#### Discussion

The bytes in the `CFData` correspond to how they are serialized in the file.

## Parameters

- `allocator`: The allocator to use for creating the identifier.
- `identifier`: The identifier to be inspected.
- `keyOut`: Upon return, a pointer to the key data that was used to create the identifier.

## See Also

- [func CMMetadataCreateIdentifierForKeyAndKeySpace(allocator: CFAllocator?, key: CFTypeRef, keySpace: CFString, identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus](cmmetadatacreateidentifierforkeyandkeyspace(allocator:key:keyspace:identifierout:).md)
  Creates a URL-like string identifier that represents a key or keyspace tuple.
- [func CMMetadataCreateKeyFromIdentifier(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus](cmmetadatacreatekeyfromidentifier(allocator:identifier:keyout:).md)
  Creates a copy of the key by using an identifier.
- [func CMMetadataCreateKeySpaceFromIdentifier(allocator: CFAllocator?, identifier: CFString, keySpaceOut: UnsafeMutablePointer<CFString?>) -> OSStatus](cmmetadatacreatekeyspacefromidentifier(allocator:identifier:keyspaceout:).md)
  Creates a copy of the keyspace by using an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatacreatekeyfromidentifierascfdata(allocator:identifier:keyout:))*