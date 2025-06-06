# decodeClassName(_:asClassName:)

**Framework**: Foundation  
**Kind**: method

Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func decodeClassName(_ inArchiveName: String, asClassName trueName: String)
```

#### Discussion

This method enables easy conversion of unarchived data when the name of a class has changed since the archive was created.

Note that there is also an instance method of the same name. An instance of `NSUnarchiver` can maintain its own mapping of class names. However, if both the class method and the instance method have been invoked using an identical value for `nameInArchive`, the class method takes precedence.

## Parameters

- `inArchiveName`: The ostensible name of a class in an archive.
- `trueName`: The name of the class to use when instantiating objects whose ostensible class, according to the archived data, is  .

## See Also

- [class func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func replace(Any, with: Any)](nsunarchiver/replace(_:with:).md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/decodeclassname(_:asclassname:)-swift.type.method)*