# nsSortDescriptors

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The request’s sort descriptors, accessed as reference types.

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
var nsSortDescriptors: [NSSortDescriptor]
```

#### Discussion

Set this configuration value to cause a [`SectionedFetchRequest`](../../sectionedfetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](../../../Foundation/nssortdescriptor.md) instances. If you want to use [`SortDescriptor`](../../../Foundation/sortdescriptor.md) instances, set [`sortDescriptors`](./sortdescriptors.md) instead. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](../configuration.md).

Access this value for a given request by using the [`nsSortDescriptors`](../../sectionedfetchresults/nssortdescriptors.md) property on the associated [`SectionedFetchResults`](../../sectionedfetchresults.md) instance, either directly or with a [`Binding`](../../binding.md).

## See Also

### Setting sort descriptors
- [var sortDescriptors: [SortDescriptor<Result>]](./sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/nssortdescriptors)*