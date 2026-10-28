# alwaysUsesMultipleValuesMarker

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected

**Availability**:
- macOS

## Declaration

```swift
var alwaysUsesMultipleValuesMarker: Bool { get set }
```

```objc
@property BOOL alwaysUsesMultipleValuesMarker;
```

## Discussion

The default is [`false`](../../Swift/false.md). Setting to [`true`](../../Swift/true.md) can increase performance if your application doesn’t allow editing multiple values. This property is observable using key-value observing.

## See Also

### Selection Attributes
- [var avoidsEmptySelection: Bool](./avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var preservesSelection: Bool](./preservesselection.md)
  A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/alwaysusesmultiplevaluesmarker)*