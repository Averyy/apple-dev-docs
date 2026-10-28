# sortDescriptors

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The request’s sort descriptors, accessed as value types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var sortDescriptors: [SortDescriptor<Result>] { get set }
```

Available when `SectionIdentifier` conforms to `Hashable` and `Result` inherits `NSManagedObject`.

## Discussion

Set this configuration value to cause a [`SectionedFetchRequest`](../../sectionedfetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](../../../Foundation/sortdescriptor.md) instances. If you want to use [`NSSortDescriptor`](../../../Foundation/nssortdescriptor.md) instances, set [`nsSortDescriptors`](./nssortdescriptors.md) instead. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](../configuration.md).

Access this value for a given request by using the [`sortDescriptors`](../../sectionedfetchresults/sortdescriptors.md) property on the associated [`SectionedFetchResults`](../../sectionedfetchresults.md) instance, either directly or with a [`Binding`](../../binding.md).

## See Also

### Setting sort descriptors
- [var nsSortDescriptors: [NSSortDescriptor]](./nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/sortdescriptors)*