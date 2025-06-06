# currentModel

**Framework**: Core Data  
**Kind**: property

The reference that represents the migration’s source model.

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
var currentModel: NSManagedObjectModelReference { get }
```

#### Discussion

Core Data sets this property to the `currentModel` parameter you specify when creating the migration stage.

## See Also

- [var nextModel: NSManagedObjectModelReference](nscustommigrationstage/nextmodel.md)
  The reference that represents the migration’s destination model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscustommigrationstage/currentmodel)*