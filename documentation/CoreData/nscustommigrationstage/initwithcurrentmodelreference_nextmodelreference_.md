# initWithCurrentModelReference:nextModelReference:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Creates a custom migration stage with the specified source and destination model references.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithCurrentModelReference:(NSManagedObjectModelReference *) currentModel nextModelReference:(NSManagedObjectModelReference *) nextModel;
```

## Return Value

An initialized custom migration stage, or `nil` if Core Data can’t create one.

## Parameters

- `currentModel`: The reference that represents the migration’s source model.
- `nextModel`: The reference that represents the migration’s destination model.

## See Also

### Creating a custom migration stage
- [class NSManagedObjectModelReference](../nsmanagedobjectmodelreference.md)
  An object that describes a specific version of an object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/initwithcurrentmodelreference:nextmodelreference:)*