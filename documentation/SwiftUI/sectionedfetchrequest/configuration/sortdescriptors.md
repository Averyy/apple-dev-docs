# sortDescriptors

**Framework**: SwiftUI  
**Kind**: property

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

#### Discussion

Set this configuration value to cause a [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances. If you want to use [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances, set [`nsSortDescriptors`](sectionedfetchrequest/configuration/nssortdescriptors.md) instead. Use care to coordinate section and sort updates, as described in [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md).

Access this value for a given request by using the [`sortDescriptors`](sectionedfetchresults/sortdescriptors.md) property on the associated [`SectionedFetchResults`](sectionedfetchresults.md) instance, either directly or with a [`Binding`](binding.md).

## See Also

- [var nsSortDescriptors: [NSSortDescriptor]](sectionedfetchrequest/configuration/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/sortdescriptors)*