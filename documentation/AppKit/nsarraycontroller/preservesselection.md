# preservesSelection

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes

**Availability**:
- macOS ?+

## Declaration

```swift
var preservesSelection: Bool { get set }
```

#### Discussion

The default is [`true`](https://developer.apple.com/documentation/Swift/true). This property is observable using key-value observing.

## See Also

- [var avoidsEmptySelection: Bool](nsarraycontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var alwaysUsesMultipleValuesMarker: Bool](nsarraycontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/preservesselection)*