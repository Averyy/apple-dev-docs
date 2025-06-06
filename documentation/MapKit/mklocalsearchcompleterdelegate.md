# MKLocalSearchCompleterDelegate

**Framework**: MapKit  
**Kind**: protocol

Methods the delegate calls with search completion data.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
protocol MKLocalSearchCompleterDelegate : NSObjectProtocol
```

#### Overview

You use this protocol when implementing an autocomplete solution for a map in your app. As the user types search terms, use an [`MKLocalSearchCompleter`](mklocalsearchcompleter.md) object to start searching for valid completions. The delegate you assign to that object needs to conform to this protocol. As it receives completions, the local search completer calls the methods of this protocol to deliver the results.

## Topics

### Getting the search results
- [func completerDidUpdateResults(MKLocalSearchCompleter)](mklocalsearchcompleterdelegate/completerdidupdateresults(_:).md)
  Tells the method when the specified search completer updates its array of search completions.
- [func completer(MKLocalSearchCompleter, didFailWithError: any Error)](mklocalsearchcompleterdelegate/completer(_:didfailwitherror:).md)
  Tells the method when the specified search completer is unable to generate a list of search results.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any MKLocalSearchCompleterDelegate)?](mklocalsearchcompleter/delegate.md)
  The object that receives the completion results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate)*