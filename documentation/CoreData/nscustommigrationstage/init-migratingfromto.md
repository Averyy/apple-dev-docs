# init(migratingFrom:to:)

**Framework**: Core Data  
**Kind**: init

Creates a custom migration stage with the specified source and destination model references.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Swift 5.8+

## Declaration

```swift
convenience init(migratingFrom currentModel: NSManagedObjectModelReference, to nextModel: NSManagedObjectModelReference)
```

## Parameters

- `currentModel`: The reference that represents the migration’s source model.
- `nextModel`: The reference that represents the migration’s destination model.

## See Also

- [class NSManagedObjectModelReference](nsmanagedobjectmodelreference.md)
  An object that describes a specific version of an object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/init(migratingfrom:to:))*