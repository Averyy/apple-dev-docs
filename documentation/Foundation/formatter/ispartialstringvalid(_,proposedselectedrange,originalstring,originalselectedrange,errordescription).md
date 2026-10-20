# isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).

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
func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafeMutablePointer<NSString>, proposedSelectedRange proposedSelRangePtr: NSRangePointer?, originalString origString: String, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

```objc
- (BOOL) isPartialStringValid:(NSString **) partialStringPtr proposedSelectedRange:(NSRangePointer) proposedSelRangePtr originalString:(NSString *) origString originalSelectedRange:(NSRange) origSelRange errorDescription:(NSString **) error;
```

#### Return Value

[`true`](../../Swift/true.md) if `partialStringPtr` is acceptable, otherwise [`false`](../../Swift/false.md).

#### Discussion

In a subclass implementation, evaluate `partialString` according to the context. Return [`true`](../../Swift/true.md) if `partialStringPtr` is acceptable and [`false`](../../Swift/false.md) if `partialStringPtr` is unacceptable. If you return [`false`](../../Swift/false.md) and assign a new string to `partialStringPtr` and a new range to `proposedSelRangePtr`, the string and selection range are changed, otherwise, if no values are assigned to `partialStringPtr` or `proposedSelRangePtr`, the change is rejected. If you return [`false`](../../Swift/false.md), you can also return by indirection an `NSString` object (in `error`) that explains the reason why the validation failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToValidatePartialString:errorDescription:.

## Parameters

- `partialStringPtr`: The new string to validate.
- `proposedSelRangePtr`: The selection range that will be used if the string is accepted or replaced.
- `origString`: The original string, before the proposed change.
- `origSelRange`: The selection range over which the change is to take place.

  If the user change is a deletion, `origSelRange` contains the range of the deleted characters.
- `error`: If non-`nil`, if validation fails contains an `NSString` object that describes the problem.

## See Also

### Validating Partial Strings
- [func isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./ispartialstringvalid%28_,neweditingstring,errordescription%29.md)
  Returns a Boolean value that indicates whether a partial string is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:))*