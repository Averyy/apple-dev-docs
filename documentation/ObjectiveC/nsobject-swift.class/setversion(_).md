# setVersion(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Sets the receiver’s version number.

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
class func setVersion(_ aVersion: Int)
```

```objc
+ (void) setVersion:(NSInteger) aVersion;
```

## Discussion

The version number is helpful when instances of the class are to be archived and reused later. The default version is `0`.

### Special Considerations

The version number applies to `NSArchiver`/`NSUnarchiver`, but not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## Parameters

- `aVersion`: The version number for the receiver.

## See Also

### Archiving
- [func awakeAfter(using: NSCoder) -> Any?](./awakeafter%28using%29.md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
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
- [class func version() -> Int](./version%28%29.md)
  Returns the version number assigned to the class.
- [classForPortCoder](./classforportcoder.md)
  Class to substitute for the receiver in distribution encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setversion(_:))*