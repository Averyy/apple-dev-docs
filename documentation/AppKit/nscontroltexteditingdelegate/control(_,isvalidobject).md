# control(_:isValidObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the insertion point leaves a cell belonging to the specified control, but before the value of the cell’s object is displayed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, isValidObject obj: Any?) -> Bool
```

```objc
- (BOOL) control:(NSControl *) control isValidObject:(id) obj;
```

#### Return Value

[`true`](../../Swift/true.md) if you want to allow the control to display the specified value; otherwise, [`false`](../../Swift/false.md) to reject the value and return the cursor to the control’s cell.

#### Discussion

This method gives the delegate the opportunity to validate the contents of the control’s cell (or selected cell). In validating, the delegate should check the value in the `object` parameter and determine if it falls within a permissible range, has required attributes, accords with a given context, and so on. Examples of objects subject to such evaluations are an `NSDate` object that should not represent a future date or a monetary amount (represented by an `NSNumber` object) that exceeds a predetermined limit.

## Parameters

- `control`: The control whose object value needs to be validated.
- `obj`: The object value to validate.

## See Also

### Related Documentation
- [protocol NSControlTextEditingDelegate](../nscontroltexteditingdelegate.md)
  A set of optional methods implemented by delegates of [`NSControl`](../nscontrol.md) subclasses to respond to editing actions.
### Validating a Control’s Value
- [func control(NSControl, didFailToValidatePartialString: String, errorDescription: String?)](./control%28_,didfailtovalidatepartialstring,errordescription%29.md)
  Invoked when the formatter for the cell belonging to `control` (or selected cell) rejects a partial string a user is typing into the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:isvalidobject:))*