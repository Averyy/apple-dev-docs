# isPartialStringValid(_:newEditingString:errorDescription:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a partial string is valid.

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
func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `partialString` is an acceptable value, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is invoked each time the user presses a key while the cell has the keyboard focus—it lets you verify and edit the cell text as the user types it.

In a subclass implementation, evaluate `partialString` according to the context, edit the text if necessary, and return by reference any edited string in `newString`. Return [`true`](https://developer.apple.com/documentation/swift/true) if `partialString` is acceptable and [`false`](https://developer.apple.com/documentation/swift/false) if `partialString` is unacceptable. If you return [`false`](https://developer.apple.com/documentation/swift/false) and `newString` is `nil`, the cell displays `partialString` minus the last character typed. If you return [`false`](https://developer.apple.com/documentation/swift/false), you can also return by indirection an `NSString` object (in `error`) that explains the reason why the validation failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToValidatePartialString:errorDescription:. The selection range will always be set to the end of the text if replacement occurs.

This method is a compatibility method. If a subclass overrides this method and does not override [`isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)`](formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:).md), this method will be called as before ([`isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)`](formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:).md) just calls this one by default).

## Parameters

- `partialString`: The text currently in a cell.
- `newString`: If   needs to be modified, upon return contains the replacement string.
- `error`: If non- , if validation fails contains an   object that describes the problem.

## See Also

- [func isPartialStringValid(AutoreleasingUnsafeMutablePointer<NSString>, proposedSelectedRange: NSRangePointer?, originalString: String, originalSelectedRange: NSRange, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:).md)
  This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/ispartialstringvalid(_:neweditingstring:errordescription:))*