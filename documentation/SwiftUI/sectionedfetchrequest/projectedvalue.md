# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A binding to the request’s mutable configuration properties.

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
@preconcurrency var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier, Result>.Configuration> { get }
```

#### Discussion

This property behaves like the [`projectedValue`](fetchrequest/projectedvalue.md) of a [`FetchRequest`](fetchrequest.md). In particular, SwiftUI returns the value associated with this property when you use [`SectionedFetchRequest`](sectionedfetchrequest.md) as a property wrapper on a [`SectionedFetchResults`](sectionedfetchresults.md) instance and then access the results with a dollar sign (`$`) prefix. The value that SwiftUI returns is a [`Binding`](binding.md) to the request’s [`SectionedFetchRequest.Configuration`](sectionedfetchrequest/configuration.md) structure, which dynamically configures the request.

## See Also

- [SectionedFetchRequest.Configuration](sectionedfetchrequest/configuration.md)
  The request’s configurable properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/projectedvalue)*