# control(_:didFailToFormatString:errorDescription:)

**Framework**: AppKit  
**Kind**: method

Invoked when the formatter for the cell belonging to the specified control cannot convert a string to an underlying object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, didFailToFormatString string: String, errorDescription error: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value in the string parameter should be accepted as is; otherwise, [`false`](https://developer.apple.com/documentation/swift/false) if the value in the parameter should be rejected.

#### Discussion

Your implementation of this method should evaluate the error or query the user an appropriate value indicating whether the string should be accepted or rejected.

## Parameters

- `control`: The control whose cell could not convert the string.
- `string`: The string that could not be converted.
- `error`: A localized, user-presentable string that explains why the conversion failed.

## See Also

- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../foundation/formatter/1408927-getobjectvalue.md)
  The default implementation of this method raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:didfailtoformatstring:errordescription:))*