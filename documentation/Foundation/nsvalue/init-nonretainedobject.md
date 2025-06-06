# init(nonretainedObject:)

**Framework**: Foundation  
**Kind**: init

Creates a value object containing the specified object.

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
init(nonretainedObject anObject: Any?)
```

#### Return Value

A new value object that contains `anObject`.

#### Discussion

This method is equivalent to invoking [`init(_:withObjCType:)`](nsvalue/init(_:withobjctype:).md) in this manner:

```objc
NSValue *theValue = [NSValue value:&anObject withObjCType:@encode(void *)];
```

This method is useful if you want to add an object to a [`Collection`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) but don’t want the collection to create a strong reference to it.

## Parameters

- `anObject`: The value for the new object.

## See Also

- [init(pointer: UnsafeRawPointer?)](nsvalue/init(pointer:).md)
  Creates a value object containing the specified pointer.
- [var pointerValue: UnsafeMutableRawPointer?](nsvalue/pointervalue.md)
  Returns the value as an untyped pointer.
- [var nonretainedObjectValue: Any?](nsvalue/nonretainedobjectvalue.md)
  The value as a non-retained pointer to an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(nonretainedobject:))*