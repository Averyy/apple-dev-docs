# alwaysUsesMultipleValuesMarker

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected

**Availability**:
- macOS ?+

## Declaration

```swift
var alwaysUsesMultipleValuesMarker: Bool { get set }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/Swift/false). Setting to [`true`](https://developer.apple.com/documentation/Swift/true) can increase performance if your application doesn’t allow editing multiple values. This property is observable using key-value observing.

## See Also

- [var avoidsEmptySelection: Bool](nsarraycontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var preservesSelection: Bool](nsarraycontroller/preservesselection.md)
  A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/alwaysusesmultiplevaluesmarker)*