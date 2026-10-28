# tokenRangeAtIndex:unit:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Returns the range of the linguistic unit containing the specified character index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```objc
- (NSRange) tokenRangeAtIndex:(NSUInteger) characterIndex unit:(NLTokenUnit) unit;
```

## Return Value

The range of the substring for the linguistic unit.

## Parameters

- `characterIndex`: The character index to begin examination.
- `unit`: The linguistic unit. For possible values, see [`NLTokenUnit`](../nltokenunit.md).

## See Also

### Determining the range of a unit token
- [- tokenRangeForRange:unit:](./tokenrangeforrange_unit_.md)
  Finds the entire range of all tokens of the specified linguistic unit contained completely or partially within the specified range.
- [enum NLTokenUnit](../nltokenunit.md)
  Constants representing linguistic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tokenrangeatindex:unit:)*