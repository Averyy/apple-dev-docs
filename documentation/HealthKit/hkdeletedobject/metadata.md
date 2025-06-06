# metadata

**Framework**: HealthKit  
**Kind**: property

The metadata associated with the deleted object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

#### Discussion

The system only copies the [`HKMetadataKeySyncIdentifier`](hkmetadatakeysyncidentifier.md) and [`HKMetadataKeySyncVersion`](hkmetadatakeysyncversion.md) keys from the original object. All other metadata is lost.

For more information about the metadata’s format and content, see the [`HKObject`](hkobject.md) class’s  [`metadata`](hkobject/metadata.md) property.

## See Also

- [var uuid: UUID](hkdeletedobject/uuid.md)
  The universally unique identifier (UUID) for the HealthKit object that was deleted from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdeletedobject/metadata)*