# isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `partialStringPtr` is acceptable, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

In a subclass implementation, evaluate `partialString` according to the context. Return [`true`](https://developer.apple.com/documentation/swift/true) if `partialStringPtr` is acceptable and [`false`](https://developer.apple.com/documentation/swift/false) if `partialStringPtr` is unacceptable. If you return [`false`](https://developer.apple.com/documentation/swift/false) and assign a new string to `partialStringPtr` and a new range to `proposedSelRangePtr`, the string and selection range are changed, otherwise, if no values are assigned to `partialStringPtr` or `proposedSelRangePtr`, the change is rejected. If you return [`false`](https://developer.apple.com/documentation/swift/false), you can also return by indirection an `NSString` object (in `error`) that explains the reason why the validation failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToValidatePartialString:errorDescription:.

## Parameters

- `partialStringPtr`: The new string to validate.
- `proposedSelRangePtr`: The selection range that will be used if the string is accepted or replaced.
- `origString`: The original string, before the proposed change.
- `origSelRange`: If the user change is a deletion,   contains the range of the deleted characters.
- `error`: If non- , if validation fails contains an   object that describes the problem.

## See Also

- [func isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/ispartialstringvalid(_:neweditingstring:errordescription:).md)
  Returns a Boolean value that indicates whether a partial string is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:))*