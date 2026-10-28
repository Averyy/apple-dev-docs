# control(_:didFailToFormatString:errorDescription:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the formatter for the cell belonging to the specified control cannot convert a string to an underlying object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, didFailToFormatString string: String, errorDescription error: String?) -> Bool
```

```objc
- (BOOL) control:(NSControl *) control didFailToFormatString:(NSString *) string errorDescription:(NSString *) error;
```

## Return Value

[`true`](../../Swift/true.md) if the value in the string parameter should be accepted as is; otherwise, [`false`](../../Swift/false.md) if the value in the parameter should be rejected.

## Discussion

Your implementation of this method should evaluate the error or query the user an appropriate value indicating whether the string should be accepted or rejected.

## Parameters

- `control`: The control whose cell could not convert the string.
- `string`: The string that could not be converted.
- `error`: A localized, user-presentable string that explains why the conversion failed.

## See Also

### Related Documentation
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](../../Foundation/formatter/getobjectvalue%28_,for,errordescription%29.md)
  The default implementation of this method raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:didfailtoformatstring:errordescription:))*