# replacementObject(for:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to substitute another object for itself during keyed archiving.

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
func replacementObject(for archiver: NSKeyedArchiver) -> Any?
```

```objc
- (id) replacementObjectForKeyedArchiver:(NSKeyedArchiver *) archiver;
```

#### Return Value

The object encode instead of the receiver (if different).

#### Discussion

This method is called only if no replacement mapping for the object has been set up in the encoder (for example, due to a previous call of [`replacementObject(for:)`](./replacementobject%28for%29-60vwc.md) to that object).

## Parameters

- `archiver`: A keyed archiver creating an archive.

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
- [class func setVersion(Int)](./setversion%28_%29.md)
  Sets the receiver’s version number.
- [class func version() -> Int](./version%28%29.md)
  Returns the version number assigned to the class.
- [classForPortCoder](./classforportcoder.md)
  Class to substitute for the receiver in distribution encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-60vwc)*