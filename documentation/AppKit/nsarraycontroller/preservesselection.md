# preservesSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes

**Availability**:
- macOS

## Declaration

```swift
var preservesSelection: Bool { get set }
```

```objc
@property BOOL preservesSelection;
```

#### Discussion

The default is [`true`](../../Swift/true.md). This property is observable using key-value observing.

## See Also

### Selection Attributes
- [var avoidsEmptySelection: Bool](./avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var alwaysUsesMultipleValuesMarker: Bool](./alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/preservesselection)*