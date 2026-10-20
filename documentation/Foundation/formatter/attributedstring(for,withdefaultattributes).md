# attributedString(for:withDefaultAttributes:)

**Framework**: Foundation  
**Kind**: method

The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.

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
func attributedString(for obj: Any, withDefaultAttributes attrs: [NSAttributedString.Key : Any]? = nil) -> NSAttributedString?
```

#### Return Value

An attributed string that represents `anObject`.

#### Discussion

When implementing a subclass, return an `NSAttributedString` object if the string for display should have some attributes. For instance, you might want negative values in a financial application to appear in red text. Invoke your implementation of [`string(for:)`](formatter/string(for:).md) to get the non-attributed string, then create an `NSAttributedString` object with it (see [`init(string:)`](nsattributedstring/init(string:).md)). Use the `attributes` default dictionary to reset the attributes of the string when a change in value warrants it (for example, a negative value becomes positive) For information on creating attributed strings, see [`Attributed String Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036i).

## Parameters

- `obj`: The object for which a textual representation is returned.
- `attrs`: The default attributes to use for the returned attributed string.

## See Also

- [func string(for: Any?) -> String?](formatter/string(for:).md)
  The default implementation of this method raises an exception.
- [func editingString(for: Any) -> String?](formatter/editingstring(for:).md)
  The default implementation of this method invokes [`string(for:)`](formatter/string(for:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/attributedstring(for:withdefaultattributes:))*