# NSSearchFieldDelegate

**Framework**: AppKit  
**Kind**: protocol

A protocol that a search field delegate can use to determine when a search started or ended.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSearchFieldDelegate : NSTextFieldDelegate
```

## Topics

### Detecting the Start and End of a Search
- [func searchFieldDidStartSearching(NSSearchField)](nssearchfielddelegate/searchfielddidstartsearching(_:).md)
  The method that is called when the search field begins searching for content.
- [func searchFieldDidEndSearching(NSSearchField)](nssearchfielddelegate/searchfielddidendsearching(_:).md)
  The method that is called when the search field has ended its search for content.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTextFieldDelegate](nstextfielddelegate.md)

## See Also

- [var delegate: (any NSSearchFieldDelegate)?](nssearchfield/delegate.md)
  The delegate for the search field, or `nil` if the search field doesn’t have a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfielddelegate)*