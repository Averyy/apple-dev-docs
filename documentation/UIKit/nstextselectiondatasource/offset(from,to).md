# offset(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the offset between the two locations you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

```objc
- (NSInteger) offsetFromLocation:(id<NSTextLocation>) from toLocation:(id<NSTextLocation>) to;
```

## Parameters

- `from`: The starting location.
- `to`: The ending location.

## See Also

### Finding specific content in the selection
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](./location%28_,offsetby%29.md)
  Returns a new location using the location and offset you specify.
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](./linefragmentrange%28for,incontainerat%29.md)
  Returns the range of the line fragment that contains the point you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](./textrange%28for,enclosing%29.md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/offset(from:to:))*