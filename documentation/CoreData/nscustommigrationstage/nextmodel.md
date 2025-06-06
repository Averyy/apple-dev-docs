# nextModel

**Framework**: Core Data  
**Kind**: property

The reference that represents the migration’s destination model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var nextModel: NSManagedObjectModelReference { get }
```

#### Discussion

Core Data sets this property to the `nextModel` parameter you specify when creating the migration stage.

## See Also

- [var currentModel: NSManagedObjectModelReference](nscustommigrationstage/currentmodel.md)
  The reference that represents the migration’s source model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/nextmodel)*