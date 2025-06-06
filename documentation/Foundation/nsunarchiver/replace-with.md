# replace(_:with:)

**Framework**: Foundation  
**Kind**: method

Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func replace(_ object: Any, with newObject: Any)
```

#### Discussion

`newObject` can be of a different class from object, and the class mappings set by [`classNameDecoded(forArchiveClassName:)`](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method.md) and [`decodeClassName(_:asClassName:)`](nsunarchiver/decodeclassname(_:asclassname:)-swift.method.md) are ignored.

## Parameters

- `object`: The archived object to replace.
- `newObject`: The object with which to replace  .

## See Also

- [class func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/replace(_:with:))*