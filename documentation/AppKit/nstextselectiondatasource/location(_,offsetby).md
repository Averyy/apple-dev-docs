# location(_:offsetBy:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a new location using the location and offset you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

```objc
- (id<NSTextLocation>) locationFromLocation:(id<NSTextLocation>) location withOffset:(NSInteger) offset;
```

## Return Value

A new `NSTextLocation, or nil` when the inputs don’t produce any legal location, such as when the input is an out of bounds index.

## Discussion

The offset value can be positive or negative indicating the logical direction.

## Parameters

- `location`: The starting location in the selection.
- `offset`: An offset that describes the extent of the new location.

## See Also

### Finding specific content in the selection
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](./linefragmentrange%28for,incontainerat%29.md)
  Returns the range of the line fragment that contains the point you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](./offset%28from,to%29.md)
  Returns the offset between the two locations you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](./textrange%28for,enclosing%29.md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/location(_:offsetby:))*