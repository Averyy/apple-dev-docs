# SearchSuggestionsPlacement.Set

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An efficient set of search suggestion display modes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Set
```

## Topics

### Getting placement sets
- [static var content: SearchSuggestionsPlacement.Set](./set/content.md)
  A set containing placements with the apps main content, excluding the menu placement.
- [static var menu: SearchSuggestionsPlacement.Set](./set/menu.md)
  A set containing the menu display mode.
### Creating a set
- [init(rawValue: Int)](./set/init%28rawvalue%29.md)
  Creates a set of search suggestions from an integer.
- [var rawValue: Int](./set/rawvalue.md)
  The raw value that records the search suggestion display modes.
### Supporting types
- [SearchSuggestionsPlacement.Set.Element](./set/element.md)
  A type for the elements of the set.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchsuggestionsplacement/set)*