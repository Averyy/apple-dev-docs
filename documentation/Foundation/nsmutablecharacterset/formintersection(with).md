# formIntersection(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the receiver so it contains only characters that exist in both the receiver and another set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func formIntersection(with otherSet: CharacterSet)
```

```objc
- (void) formIntersectionWithCharacterSet:(NSCharacterSet *) otherSet;
```

## Parameters

- `otherSet`: The character set with which to perform the intersection.

## See Also

### Combining Character Sets
- [func formUnion(with: CharacterSet)](./formunion%28with%29.md)
  Modifies the receiver so it contains all characters that exist in either the receiver or another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/formintersection(with:))*