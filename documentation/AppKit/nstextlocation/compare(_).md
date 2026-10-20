# compare(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Compares and returns the logical ordering to location.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func compare(_ location: any NSTextLocation) -> ComparisonResult
```

```objc
- (NSComparisonResult) compare:(id<NSTextLocation>) location;
```

#### Return Value

A [`ComparisonResult`](../../Foundation/comparisonresult.md).

## Parameters

- `location`: The location to compare the current location to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlocation/compare(_:))*