# query

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

A value that indicates that the search completer includes query completions in the result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var query: MKLocalSearchCompleter.ResultType { get }
```

```c
MKLocalSearchCompleterResultTypeQuery
```

#### Discussion

For example, the search string `cof` yields a completion for *coffee*.

## See Also

### Type properties
- [static var address: MKLocalSearchCompleter.ResultType](./address.md)
  A value that indicates that the search completer includes address completions in the result.
- [static var pointOfInterest: MKLocalSearchCompleter.ResultType](./pointofinterest.md)
  A value that indicates that the search completer includes point-of-interest completions in the result.
- [static var physicalFeature: MKLocalSearchCompleter.ResultType](./physicalfeature.md)
  A value that indicates that the search completer includes physical feature completions in the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/resulttype/query)*