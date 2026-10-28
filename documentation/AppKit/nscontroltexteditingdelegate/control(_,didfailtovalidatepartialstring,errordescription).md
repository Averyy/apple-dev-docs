# control(_:didFailToValidatePartialString:errorDescription:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the formatter for the cell belonging to `control` (or selected cell) rejects a partial string a user is typing into the cell.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, didFailToValidatePartialString string: String, errorDescription error: String?)
```

```objc
- (void) control:(NSControl *) control didFailToValidatePartialString:(NSString *) string errorDescription:(NSString *) error;
```

## Discussion

You can implement this method to display a warning message or perform a similar action when the user enters improperly formatted text.

## Parameters

- `control`: The control whose cell rejected the string.
- `string`: The string that includes the character that caused the rejection.
- `error`: A localized, user-presentable string that explains why the string was rejected.

## See Also

### Related Documentation
- [func isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../../Foundation/formatter/ispartialstringvalid%28_,neweditingstring,errordescription%29.md)
  Returns a Boolean value that indicates whether a partial string is valid.
### Validating a Control’s Value
- [func control(NSControl, isValidObject: Any?) -> Bool](./control%28_,isvalidobject%29.md)
  Invoked when the insertion point leaves a cell belonging to the specified control, but before the value of the cell’s object is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:didfailtovalidatepartialstring:errordescription:))*