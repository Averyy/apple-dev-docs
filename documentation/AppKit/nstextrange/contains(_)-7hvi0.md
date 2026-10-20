# contains(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines if the text location you specify is in the current text range.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func contains(_ location: any NSTextLocation) -> Bool
```

```objc
- (BOOL) containsLocation:(id<NSTextLocation>) location;
```

#### Return Value

Returns `true` if the location is in the range otherwise `false` .

## Parameters

- `location`: An [`NSTextLocation`](../nstextlocation.md).

## See Also

### Finding text within the text range
- [func contains(NSTextRange) -> Bool](./contains%28_%29-5j4y2.md)
  Determines if the text range you specify is in the current text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/contains(_:)-7hvi0)*