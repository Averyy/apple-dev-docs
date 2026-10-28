# lineFragmentRange(for:inContainerAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the range of the line fragment that contains the point you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func lineFragmentRange(for point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextRange?
```

```objc
- (NSTextRange *) lineFragmentRangeForPoint:(CGPoint) point inContainerAtLocation:(id<NSTextLocation>) location;
```

## Return Value

An `NSTextRange` that describes the location of the line fragment, or nil if the range isn’t found.

## Parameters

- `point`: The starting point that contains the line fragment, in the coordinate system of `location`.
- `location`: The location of the line fragment.

## See Also

### Finding specific content in the selection
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](./location%28_,offsetby%29.md)
  Returns a new location using the location and offset you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](./offset%28from,to%29.md)
  Returns the offset between the two locations you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](./textrange%28for,enclosing%29.md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/linefragmentrange(for:incontainerat:))*