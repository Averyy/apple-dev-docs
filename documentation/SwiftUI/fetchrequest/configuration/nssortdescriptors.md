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
@MainActor
@preconcurrency var nsSortDescriptors: [NSSortDescriptor]
```

#### Discussion

Set this configuration value to cause a [`FetchRequest`](../../fetchrequest.md) to execute a fetch with a new collection of [`NSSortDescriptor`](../../../Foundation/nssortdescriptor.md) instances. If you want to use [`SortDescriptor`](../../../Foundation/sortdescriptor.md) instances, set [`sortDescriptors`](./sortdescriptors.md) instead.

Access this value of a [`FetchRequest.Configuration`](../configuration.md) structure for a given request by using the [`nsSortDescriptors`](../../fetchedresults/nssortdescriptors.md) property on the associated [`FetchedResults`](../../fetchedresults.md) instance, either directly or through a [`Binding`](../../binding.md).

## See Also

### Setting sort descriptors
- [var sortDescriptors: [SortDescriptor<Result>]](./sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/nssortdescriptors)*