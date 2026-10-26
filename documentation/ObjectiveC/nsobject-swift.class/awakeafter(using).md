# awakeAfter(using:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func awakeAfter(using coder: NSCoder) -> Any?
```

```objc
- (id) awakeAfterUsingCoder:(NSCoder *) coder;
```

#### Return Value

The receiver, or another object to take the place of the object that was decoded and subsequently received this message.

#### Discussion

You can use this method to eliminate redundant objects created by the coder. For example, if after decoding an object you discover that an equivalent object already exists, you can return the existing object. If a replacement is returned, your overriding method is responsible for releasing the receiver.

This method is invoked by `NSCoder`. `NSObject`’s implementation simply returns `self`.

## Parameters

- `coder`: The decoder used to decode the receiver.

## See Also

### Related Documentation
- [init?(coder: NSCoder)](../../Foundation/nscoding/init%28coder%29.md)
  Initializes the receiver from data in a given unarchiver.
### Archiving
- [var classForArchiver: AnyClass?](./classforarchiver.md)
  The class to substitute for the receiver’s own class during archiving.
- [var classForCoder: AnyClass](./classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](./classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classFallbacksForKeyedArchiver() -> [String]](./classfallbacksforkeyedarchiver%28%29.md)
  Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [class func classForKeyedUnarchiver() -> AnyClass](./classforkeyedunarchiver%28%29.md)
  Overridden by subclasses to substitute a new class during keyed unarchiving.
- [func replacementObject(for: NSArchiver) -> Any?](./replacementobject%28for%29-8ih2x.md)
  Overridden by subclasses to substitute another object for itself during archiving.
- [func replacementObject(for: NSCoder) -> Any?](./replacementobject%28for%29-2l8ox.md)
  Overridden by subclasses to substitute another object for itself during encoding.
- [func replacementObject(for: NSKeyedArchiver) -> Any?](./replacementobject%28for%29-60vwc.md)
  Overridden by subclasses to substitute another object for itself during keyed archiving.
- [class func setVersion(Int)](./setversion%28_%29.md)
  Sets the receiver’s version number.
- [class func version() -> Int](./version%28%29.md)
  Returns the version number assigned to the class.
- [classForPortCoder](./classforportcoder.md)
  Class to substitute for the receiver in distribution encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/awakeafter(using:))*