# control(_:isValidObject:)

**Framework**: AppKit  
**Kind**: method

Invoked when the insertion point leaves a cell belonging to the specified control, but before the value of the cell’s object is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, isValidObject obj: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you want to allow the control to display the specified value; otherwise, [`false`](https://developer.apple.com/documentation/swift/false) to reject the value and return the cursor to the control’s cell.

#### Discussion

This method gives the delegate the opportunity to validate the contents of the control’s cell (or selected cell). In validating, the delegate should check the value in the `object` parameter and determine if it falls within a permissible range, has required attributes, accords with a given context, and so on. Examples of objects subject to such evaluations are an `NSDate` object that should not represent a future date or a monetary amount (represented by an `NSNumber` object) that exceeds a predetermined limit.

## Parameters

- `control`: The control whose object value needs to be validated.
- `obj`: The object value to validate.

## See Also

- [Control and Cell Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/ControlCell.html#//apple_ref/doc/uid/10000015i)
- [func control(NSControl, didFailToValidatePartialString: String, errorDescription: String?)](nscontroltexteditingdelegate/control(_:didfailtovalidatepartialstring:errordescription:).md)
  Invoked when the formatter for the cell belonging to `control` (or selected cell) rejects a partial string a user is typing into the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:isvalidobject:))*