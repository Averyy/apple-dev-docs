# listSectionMargins(_:_:)

**Framework**: FamilyControls  
**Kind**: method

Set the section margins for the specific edges.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func listSectionMargins(_ edges: Edge.Set = .all, _ length: CGFloat?) -> some View
```

#### Return Value

A view in which the margins of list sections are set to the specified amount on the specified edges.

#### Discussion

Use this modifier on a list section to set customize its margins. Indicate the edges to set the margin of by naming either a single value from  `Edge/Set`, or by specifying an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that contains edge values. Margins for the other edges remain unchanged.

The default section margins are based on the list style, list section spacing and content margins of the list. Using this modifier overrides these default values completely.

For sections that have headers or footers, the section margins are applied around these.

## Parameters

- `edges`: The set of edges to pad for sections in this view. The   default is  .
- `length`: An amount, given in points, to pad section on the   specified edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/listsectionmargins(_:_:))*