# makeBinaryArchive(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a Metal binary archive instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeBinaryArchive(descriptor: MTLBinaryArchiveDescriptor) throws -> any MTLBinaryArchive
```

## Mentions

- [Compiling Binary Archives from a Custom Configuration Script](compiling-binary-archives-from-a-custom-configuration-script.md)
- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

## Parameters

- `descriptor`: An   instance.

## See Also

- [class MTLBinaryArchiveDescriptor](mtlbinaryarchivedescriptor.md)
  A description of a binary shader archive that you want to create.
- [MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/code.md)
  Error codes when creating binary archives of compiled shader code.
- [let MTLBinaryArchiveDomain: String](mtlbinaryarchivedomain.md)
  The domain for Metal binary archive errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebinaryarchive(descriptor:))*