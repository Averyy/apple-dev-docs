# classForPortCoder

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

Class to substitute for the receiver in distribution encoding.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (readonly) Class classForPortCoder;
```

#### Discussion

This property allows specialized behavior for distributed objects—override [`classForCoder`](./classforcoder.md) to add general coding behavior.

## See Also

### Related Documentation
- [- replacementObjectForPortCoder:](./replacementobjectforportcoder_.md)
  Overridden by subclasses to substitute another object or a copy for itself during distribution encoding.
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
- [class func setVersion(Int)](./setversion%28_%29.md)
  Sets the receiver’s version number.
- [class func version() -> Int](./version%28%29.md)
  Returns the version number assigned to the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforportcoder)*