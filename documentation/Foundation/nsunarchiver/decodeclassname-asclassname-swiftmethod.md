# decodeClassName(_:asClassName:)

**Framework**: Foundation  
**Kind**: method

Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func decodeClassName(_ inArchiveName: String, asClassName trueName: String)
```

#### Discussion

This method enables easy conversion of unarchived data when the name of a class has changed since the archive was created.

Note that there’s also a class method of the same name. The class method has precedence in case of conflicts.

## Parameters

- `inArchiveName`: The ostensible name of a class in an archive.
- `trueName`: The name of the class to use when instantiating objects whose ostensible class, according to the archived data, is  .

## See Also

- [class func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func replace(Any, with: Any)](nsunarchiver/replace(_:with:).md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/decodeclassname(_:asclassname:)-swift.method)*