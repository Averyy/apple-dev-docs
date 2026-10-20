# classNameDecoded(forArchiveClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
class func classNameDecoded(forArchiveClassName inArchiveName: String) -> String
```

```objc
+ (NSString *) classNameDecodedForArchiveClassName:(NSString *) inArchiveName;
```

#### Return Value

The name of the class used when instantiating objects whose ostensible class, according to the archived data, is `nameInArchive`. Returns `nameInArchive` if no substitute name has been specified using the class method (not the instance method) [`decodeClassName(_:asClassName:)`](./decodeclassname%28_,asclassname%29-swift.type.method.md).

#### Discussion

Note that each individual instance of `NSUnarchiver` can be given its own class name mappings by invoking the instance method [`decodeClassName(_:asClassName:)`](./decodeclassname%28_,asclassname%29-swift.method.md). The `NSUnarchiver` class has no information about these instance-specific mappings, however, so they don’t affect the return value of [`classNameDecoded(forArchiveClassName:)`](./classnamedecoded%28forarchiveclassname%29-swift.type.method.md).

## Parameters

- `inArchiveName`: The name of a class.

## See Also

### Substituting classes or objects
- [class func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](./classnamedecoded%28forarchiveclassname%29-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func replace(Any, with: Any)](./replace%28_,with%29.md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method)*