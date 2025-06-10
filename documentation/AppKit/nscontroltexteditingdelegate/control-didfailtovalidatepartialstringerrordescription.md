# control(_:didFailToValidatePartialString:errorDescription:)

**Framework**: AppKit  
**Kind**: method

Invoked when the formatter for the cell belonging to `control` (or selected cell) rejects a partial string a user is typing into the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, didFailToValidatePartialString string: String, errorDescription error: String?)
```

#### Discussion

You can implement this method to display a warning message or perform a similar action when the user enters improperly formatted text.

## Parameters

- `control`: The control whose cell rejected the string.
- `string`: The string that includes the character that caused the rejection.
- `error`: A localized, user-presentable string that explains why the string was rejected.

## See Also

- [func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../Foundation/Formatter/isPartialStringValid(_:newEditingString:errorDescription:).md)
  Returns a Boolean value that indicates whether a partial string is valid.
- [func control(NSControl, isValidObject: Any?) -> Bool](nscontroltexteditingdelegate/control(_:isvalidobject:).md)
  Invoked when the insertion point leaves a cell belonging to the specified control, but before the value of the cell’s object is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:didfailtovalidatepartialstring:errordescription:))*