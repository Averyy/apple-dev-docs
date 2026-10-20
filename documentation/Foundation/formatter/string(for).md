# string(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

The default implementation of this method raises an exception.

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
func string(for obj: Any?) -> String?
```

```objc
- (NSString *) stringForObjectValue:(id) obj;
```

#### Return Value

An `NSString` object that textually represents `object` for display. Returns `nil` if `object` is not of the correct class.

#### Discussion

When implementing a subclass, return the `NSString` object that textually represents the cell’s object for display and—if [`editingString(for:)`](./editingstring%28for%29.md) is unimplemented—for editing. First test the passed-in object to see if it’s of the correct class. If it isn’t, return `nil`; but if it is of the right class, return a properly formatted and, if necessary, localized string. (See the specification of the [`NSString`](../nsstring.md) class for formatting and localizing details.)

The following implementation (which is paired with the [`getObjectValue(_:for:errorDescription:)`](./getobjectvalue%28_,for,errordescription%29.md) example above) prefixes a two-digit float representation with a dollar sign:

```objc
- (NSString *)stringForObjectValue:(id)anObject {
 
    if (![anObject isKindOfClass:[NSNumber class]]) {
        return nil;
    }
    return [NSString stringWithFormat:@"$%.2f", [anObject  floatValue]];
}
```

## Parameters

- `obj`: The object for which a textual representation is returned.

## See Also

### Related Documentation
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getobjectvalue%28_,for,errordescription%29.md)
  The default implementation of this method raises an exception.
### Getting Textual Representations of Object Values
- [func attributedString(for: Any, withDefaultAttributes: [NSAttributedString.Key : Any]?) -> NSAttributedString?](./attributedstring%28for,withdefaultattributes%29.md)
  The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.
- [func editingString(for: Any) -> String?](./editingstring%28for%29.md)
  The default implementation of this method invokes [`string(for:)`](./string%28for%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/string(for:))*