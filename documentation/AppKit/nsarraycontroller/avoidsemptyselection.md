# avoidsEmptySelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection

**Availability**:
- macOS

## Declaration

```swift
var avoidsEmptySelection: Bool { get set }
```

```objc
@property BOOL avoidsEmptySelection;
```

## Discussion

The default is [`true`](../../Swift/true.md). This property is observable using key-value observing.

## See Also

### Selection Attributes
- [var preservesSelection: Bool](./preservesselection.md)
  A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes
- [var alwaysUsesMultipleValuesMarker: Bool](./alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/avoidsemptyselection)*