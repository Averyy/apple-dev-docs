# init(forConjunction:children:)

**Framework**: Address Book  
**Kind**: init

Returns a compound search element, created by combining the search elements in an array with the given conjunction.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(forConjunction conjuction: ABSearchConjunction, children: [Any]!)
```

#### Return Value

A compound search element, created by combining the given search elements with the given conjunction

#### Discussion

The objects in the `children` array must be `ABSearchElement` objects. The conjunction can be `kABSearchAnd` or `kABSearchOr`. If `children` is `nil` or empty, this method raises an exception.

## Parameters

- `conjuction`: The logical operator with which to combine the search elements.
- `children`: An array of search elements to be combined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchelement/init(forconjunction:children:))*