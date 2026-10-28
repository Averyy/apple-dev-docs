# tokenRangeForRange:unit:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSRange) tokenRangeForRange:(NSRange) range unit:(NLTokenUnit) unit;
```

## Return Value

The smallest possible range that contains all of the tokens of the specified linguistic unit within the range specified in `range`. This result includes a token’s entire range if any part of that token is included within `range`. If the length of `range` is 0, this return value is equivalent to [`tokenRangeAtIndex:unit:`](./tokenrangeatindex_unit_.md).

## Parameters

- `range`: The range within the string to search for tokens.
- `unit`: The linguistic unit. For possible values, see [`NLTokenUnit`](../nltokenunit.md).

## See Also

### Determining the range of a unit token
- [- tokenRangeAtIndex:unit:](./tokenrangeatindex_unit_.md)
  Returns the range of the linguistic unit containing the specified character index.
- [enum NLTokenUnit](../nltokenunit.md)
  Constants representing linguistic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tokenrangeforrange:unit:)*