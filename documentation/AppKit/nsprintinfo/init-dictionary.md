# init(dictionary:)

**Framework**: AppKit  
**Kind**: init

Returns a printing information object initialized with the parameters in the specified dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
init(dictionary attributes: [NSPrintInfo.AttributeKey : Any])
```

#### Return Value

An initialized `NSPrintInfo` object, or nil if the object could not be created.

#### Discussion

This method is the designated initializer for this class. Non-object values should be stored in `NSValue` objects (or an appropriate subclass like `NSNumber`) in the dictionary. See [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) for a list of types which should be stored using the `NSNumber` class; otherwise use `NSValue`.

## Parameters

- `attributes`: The possible key-value pairs contained in   are described in Constants.

## See Also

- [Printing Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_aboutprinting/osxp_aboutprt.html#//apple_ref/doc/uid/10000083i)
- [func dictionary() -> NSMutableDictionary](nsprintinfo/dictionary.md)
  Returns the print info’s dictionary that contains the printing attributes.
- [class var shared: NSPrintInfo](nsprintinfo/shared.md)
  The shared printing information object.
- [convenience init()](nsprintinfo/init.md)
  Creates a printing information object.
- [init(coder: NSCoder)](nsprintinfo/init(coder:).md)
  Creates a printing information object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/init(dictionary:))*