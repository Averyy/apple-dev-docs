# hidesEmptyCells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the text table hides empty cells.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var hidesEmptyCells: Bool { get set }
```

```objc
@property BOOL hidesEmptyCells;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the text table hides empty cells. If empty cells are hidden, locations with empty cells allow the background of the enclosing block or text container to show through.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttable/hidesemptycells)*