# nsSortDescriptors

**Framework**: SwiftUI  
**Kind**: property

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
@MainActor
@preconcurrency var nsSortDescriptors: [NSSortDescriptor]
```

#### Discussion

Set this configuration value to cause a [`FetchRequest`](fetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) instances. If you want to use [`SortDescriptor`](https://developer.apple.com/documentation/Foundation/SortDescriptor) instances, set [`sortDescriptors`](fetchrequest/configuration/sortdescriptors.md) instead.

Access this value of a [`FetchRequest.Configuration`](fetchrequest/configuration.md) structure for a given request by using the [`nsSortDescriptors`](fetchedresults/nssortdescriptors.md) property on the associated [`FetchedResults`](fetchedresults.md) instance, either directly or through a [`Binding`](binding.md).

## See Also

- [var sortDescriptors: [SortDescriptor<Result>]](fetchrequest/configuration/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/nssortdescriptors)*