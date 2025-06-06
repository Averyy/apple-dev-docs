# nsPredicate

**Framework**: SwiftUI  
**Kind**: property

The request’s predicate.

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
var nsPredicate: NSPredicate?
```

#### Discussion

Set this configuration value to cause a [`SectionedFetchRequest`](sectionedfetchrequest.md) to execute a fetch with a new predicate.

Access this value for a given request by using the [`nsPredicate`](sectionedfetchresults/nspredicate.md) property on the associated [`SectionedFetchResults`](sectionedfetchresults.md) instance, either directly or with a [`Binding`](binding.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/nspredicate)*