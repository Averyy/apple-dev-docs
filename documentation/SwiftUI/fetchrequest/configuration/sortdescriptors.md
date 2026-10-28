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
@MainActor
@preconcurrency var sortDescriptors: [SortDescriptor<Result>] { get set }
```

Available when `Result` inherits `NSManagedObject`.

## Discussion

Set this configuration value to cause a [`FetchRequest`](../../fetchrequest.md) to execute a fetch with a new collection of [`SortDescriptor`](../../../Foundation/sortdescriptor.md) instances. If you want to use [`NSSortDescriptor`](../../../Foundation/nssortdescriptor.md) instances, set [`nsSortDescriptors`](./nssortdescriptors.md) instead.

Access this value of a [`FetchRequest.Configuration`](../configuration.md) structure for a given request by using the [`sortDescriptors`](../../fetchedresults/sortdescriptors.md) property on the associated [`FetchedResults`](../../fetchedresults.md) instance, either directly or through a [`Binding`](../../binding.md).

## See Also

### Setting sort descriptors
- [var nsSortDescriptors: [NSSortDescriptor]](./nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/sortdescriptors)*