# SearchCriteria

**Framework**: App Intents  
**Kind**: protocol

An interface for defining the criteria to use when searching your app’s content.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
protocol SearchCriteria : _IntentValue, Hashable, Sendable
```

#### Overview

The system uses this protocol to define the search criteria it supports. Use only the system-defined types that adopt this protocol, and don’t adopt this protocol in your own types.

## Topics

### Associated Types
- [associatedtype SearchScopes = Void](searchcriteria/searchscopes.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [StringSearchCriteria](stringsearchcriteria.md)

## See Also

- [var criteria: Self.Criteria](showinappsearchresultsintent/criteria-swift.property.md)
  The information to use when performing the search.
- [struct StringSearchCriteria](stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/searchcriteria)*