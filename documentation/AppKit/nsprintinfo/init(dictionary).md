# init(dictionary:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a printing information object initialized with the parameters in the specified dictionary.

**Availability**:
- macOS

## Declaration

```swift
init(dictionary attributes: [NSPrintInfo.AttributeKey : Any])
```

```objc
- (instancetype) initWithDictionary:(NSDictionary<NSString *,id> *) attributes;
```

## Return Value

An initialized `NSPrintInfo` object, or nil if the object could not be created.

## Discussion

This method is the designated initializer for this class. Non-object values should be stored in `NSValue` objects (or an appropriate subclass like `NSNumber`) in the dictionary. See [`NSNumber`](../../Foundation/nsnumber.md) for a list of types which should be stored using the `NSNumber` class; otherwise use `NSValue`.

## Parameters

- `attributes`: The possible key-value pairs contained in `aDictionary` are described in Constants.

## See Also

### Related Documentation
- [class NSPrintInfo](../nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [func dictionary() -> NSMutableDictionary](./dictionary%28%29.md)
  Returns the print info’s dictionary that contains the printing attributes.
### Creating the Printing Information Object
- [class var shared: NSPrintInfo](./shared.md)
  The shared printing information object.
- [convenience init()](./init%28%29.md)
  Creates a printing information object.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a printing information object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/init(dictionary:))*