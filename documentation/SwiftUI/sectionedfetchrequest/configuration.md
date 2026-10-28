# SectionedFetchRequest.Configuration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The request’s configurable properties.

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
struct Configuration
```

## Overview

You initialize a [`SectionedFetchRequest`](../sectionedfetchrequest.md) with a section identifier, an optional predicate, and sort descriptors, either explicitly or with a configured [`NSFetchRequest`](../../CoreData/nsfetchrequest.md). Later, you can dynamically update the identifier, predicate, and sort parameters using the request’s configuration structure.

You access or bind to a request’s configuration components through properties on the associated [`SectionedFetchResults`](../sectionedfetchresults.md) instance, just like you do for a [`FetchRequest`](../fetchrequest.md) using [`FetchRequest.Configuration`](../fetchrequest/configuration.md).

When configuring a sectioned fetch request, ensure that the combination of the section identifier and the primary sort descriptor doesn’t create discontiguous sections.

## Topics

### Setting the section identifier
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](./configuration/sectionidentifier.md)
  The request’s section identifier key path.
### Setting a predicate
- [var nsPredicate: NSPredicate?](./configuration/nspredicate.md)
  The request’s predicate.
### Setting sort descriptors
- [var sortDescriptors: [SortDescriptor<Result>]](./configuration/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](./configuration/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically
- [var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier, Result>.Configuration>](./projectedvalue.md)
  A binding to the request’s mutable configuration properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration)*