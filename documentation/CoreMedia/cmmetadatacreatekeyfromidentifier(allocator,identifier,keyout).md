# CMMetadataCreateKeyFromIdentifier(allocator:identifier:keyOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a copy of the key by using an identifier.

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
func CMMetadataCreateKeyFromIdentifier(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFTypeRef?>) -> OSStatus
```

```c
extern OSStatus CMMetadataCreateKeyFromIdentifier(CFAllocatorRef allocator, CFStringRef identifier, CFTypeRef*keyOut);
```

#### Return Value

If successful, a nonzero result code. See [Metadata Identifier Error Codes](./metadata-identifier-errors.md).

#### Discussion

The returned `CFType` is based on the keyspace encoded in the identifier.

For `OSType` keyspaces, the key will be returned as a `CFNumber`, where a big endian interpretation of its [`CFNumberType.sInt32Type`](../CoreFoundation/cfnumbertype/sint32type.md) value represents the four bytes of the key’s numeric value.

For the keyspaces [`kCMMetadataKeySpace_QuickTimeMetadata`](./kcmmetadatakeyspace_quicktimemetadata.md) and [`kCMMetadataKeySpace_Icy`](./kcmmetadatakeyspace_icy.md), the key will be returned as a `CFString`.

All other keyspaces will have the function return the key as a `CFData`.

## Parameters

- `allocator`: The allocator to use for creating the identifier.
- `identifier`: The identifier to be inspected.
- `keyOut`: Upon return, a pointer to the key data that was used to create the identifier.

## See Also

### Creating Metadata Identifiers
- [func CMMetadataCreateIdentifierForKeyAndKeySpace(allocator: CFAllocator?, key: CFTypeRef, keySpace: CFString, identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus](./cmmetadatacreateidentifierforkeyandkeyspace%28allocator,key,keyspace,identifierout%29.md)
  Creates a URL-like string identifier that represents a key or keyspace tuple.
- [func CMMetadataCreateKeyFromIdentifierAsCFData(allocator: CFAllocator?, identifier: CFString, keyOut: UnsafeMutablePointer<CFData?>) -> OSStatus](./cmmetadatacreatekeyfromidentifierascfdata%28allocator,identifier,keyout%29.md)
  Creates a copy of the key by using an identifier, and results in a core foundation data object.
- [func CMMetadataCreateKeySpaceFromIdentifier(allocator: CFAllocator?, identifier: CFString, keySpaceOut: UnsafeMutablePointer<CFString?>) -> OSStatus](./cmmetadatacreatekeyspacefromidentifier%28allocator,identifier,keyspaceout%29.md)
  Creates a copy of the keyspace by using an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmetadatacreatekeyfromidentifier(allocator:identifier:keyout:))*